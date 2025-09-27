import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title='Recommend Apartments')

location_df = pickle.load(open('C:/Users/SWAPN/OneDrive/Desktop/DS_projet/RealEstate-Capstone-Analytics/location_distance.pkl' , 'rb'))
cosine_sim1 = pickle.load(open('C:/Users/SWAPN/OneDrive/Desktop/DS_projet/RealEstate-Capstone-Analytics/cosine_sim1.pkl' , 'rb'))
cosine_sim2 = pickle.load(open('C:/Users/SWAPN/OneDrive/Desktop/DS_projet/RealEstate-Capstone-Analytics/cosine_sim2.pkl' , 'rb'))
cosine_sim3 = pickle.load(open('C:/Users/SWAPN/OneDrive/Desktop/DS_projet/RealEstate-Capstone-Analytics/cosine_sim3.pkl' , 'rb'))
# import os
# import pickle

# # Base directory relative to the current script
# BASE_DIR = os.path.join(os.path.dirname(__file__), '..')

# # Load all your .pkl files using relative paths
# location_path = os.path.join(BASE_DIR, 'location_distance.pkl')
# with open(location_path, 'rb') as f:
#     location_df = pickle.load(f)

# cosine_sim1_path = os.path.join(BASE_DIR, 'cosine_sim1.pkl')
# with open(cosine_sim1_path, 'rb') as f:
#     cosine_sim1 = pickle.load(f)

# cosine_sim2_path = os.path.join(BASE_DIR, 'cosine_sim2.pkl')
# with open(cosine_sim2_path, 'rb') as f:
#     cosine_sim2 = pickle.load(f)

# cosine_sim3_path = os.path.join(BASE_DIR, 'cosine_sim3.pkl')
# with open(cosine_sim3_path, 'rb') as f:
#     cosine_sim3 = pickle.load(f)


def recommend_properties_with_scores(property_name, top_n=247):
    cosine_sim_matrix = .5 * cosine_sim1 + .8 * cosine_sim2 + cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


# Test the recommender function using a property name
recommend_properties_with_scores('DLF The Camellias')


st.title('Select Location and  Radius : ')

selected_location = st.selectbox('Location : ', sorted(location_df.columns.to_list()))

radius = st.number_input('Radius in Km : ')

if st.button('Search'):
    x = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values().to_dict()

    for key, value in x.items():
        # value = value/1000,
        st.text(str(key) + " ----> " +  str(value/1000) + "  " + 'in km')

st.title('Recommender System :')
selected_apartment = st.selectbox('Select an Apartment : ' , sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment)

    st.dataframe(recommendation_df.head())

