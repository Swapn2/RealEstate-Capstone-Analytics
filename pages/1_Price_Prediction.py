import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title = 'Viz Demo')



# Base directory relative to the current script
# with open('df.pkl' , 'rb') as file:
#     df = pickle.load(file)

# with open('pipeline.pkl' , 'rb') as file:
#     pipeline = pickle.load(file)
# # st.dataframe(df)

import pickle
import joblib
import os

import os
import joblib
import pickle

# Base directory is the parent of the pages folder
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')

# Load df.pkl
df_path = os.path.join(BASE_DIR, 'df.pkl')
with open(df_path, 'rb') as f:
    df = pickle.load(f)

# Load compressed pipeline
pipeline_path = os.path.join(BASE_DIR, 'pipeline_compressed.pkl')
pipeline = joblib.load(pipeline_path)


# st.dataframe(df)


st.header('Enter Your Inputs :)')
 # property type input
property_type = st.selectbox('Property Type :', ['flat','house'])
# sector type input
sector = st.selectbox('Sector : ',sorted(df['sector'].unique().tolist()) )

bedroom = int(st.selectbox('No. Of Bedrooms : ',sorted(df['bedRoom'].unique().tolist()) ))

bathroom = int(st.selectbox('No. Of Bathrooms : ',sorted(df['bathroom'].unique().tolist()) ))

balcony = st.selectbox('No. Of Balconies : ',sorted(df['balcony'].unique().tolist()) )

property_age = st.selectbox('Property Age: ',sorted(df['agePossession'].unique().tolist()) )

built_up_area = float(st.number_input('Built Up Area'))

servant_room = int(st.selectbox('Servant Room: ' ,[0,1]))

store_room = int(st.selectbox('Store Room: ' ,[0,1]))

furnishing_type = st.selectbox('Furnishing Type : ',sorted(df['furnishing_type'].unique().tolist()) )

luxury_category = st.selectbox('Luxury Category : ',sorted(df['luxury_category'].unique().tolist()) )

floor_category = st.selectbox('Floor Category : ',sorted(df['floor_category'].unique().tolist()) )


if st.button('Predict'):

    # form a DataFrame
    data = [[property_type, sector, bedroom, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)
    # st.dataframe(one_df)

    # Predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low_price = base_price - .22
    high_price = base_price + .22

    # display
    st.text('The Price Of the {} is between  {} Cr and  {}  Cr'.format(property_type, round(low_price,2),round(high_price,2)))


#





