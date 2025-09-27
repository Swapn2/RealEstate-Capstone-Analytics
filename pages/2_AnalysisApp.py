import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import plotly.graph_objects as go
import numpy as np
from scipy.stats import gaussian_kde



st.set_page_config(page_title='plotting Demo')

st.title('Page 1')

# feature_text = pickle.load(open('C:/Users/SWAPN/OneDrive/Desktop/DS_projet/RealEstate-Capstone-Analytics/feature_text.pkl' , 'rb'))
with open('feature_text.pkl', 'rb') as f:
    feature_text = pickle.load(f)



new_df = pd.read_csv('C:/Users/SWAPN/OneDrive/Desktop/DS_projet/RealEstate-Capstone-Analytics/data_viz1.csv')
# st.dataframe(new_df)

group_df = new_df[['sector', 'price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].groupby('sector').mean()
st.header("Sector price curve , price per sqft :")
fig = px.scatter_mapbox(group_df , lat = "latitude" , lon = "longitude", color = "price_per_sqft" , size = "built_up_area" ,
                        color_continuous_scale = px.colors.cyclical.IceFire, zoom = 9.333 ,
                        mapbox_style = "open-street-map" ,
                        width = 1200 , height = 700 ,
                        hover_name = group_df.index)
st.plotly_chart(fig , use_container_width=True)

st.header('Features Wordcloud :')
wordcloud = WordCloud(width = 800 , height = 800,
                       background_color = 'white',
                      stopwords = set(['s']),
                      min_font_size = 10).generate(feature_text)
fig1, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig1.tight_layout(pad=0)
st.pyplot(fig1)

st.header('Price v/s Built Up Area :')
property_type = st.selectbox('Select Property Type : ', ['flat' , 'house'])
if property_type == 'house':
    fig2 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color='bedRoom', title=" Area v/s Price ")
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color='bedRoom', title=" Area v/s Price ")
    st.plotly_chart(fig2, use_container_width=True)


st.header('BHK pie chart in different Sectors :')
new_list = new_df['sector'].unique().tolist()
new_list.insert(0,'overall')

sector = st.selectbox('Select Sector : ' , new_list)
if sector == 'overall':
    fig3 = px.pie(new_df, names="bedRoom")
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.pie(new_df[new_df['sector'] == sector], names="bedRoom")
    st.plotly_chart(fig3, use_container_width=True)

st.header('Side By Side BHK price comparison :')
# new_list2 = new_df['sector'].unique().tolist()
# new_list2.insert(0,'overall')

sector_box = st.selectbox('Select Sector : ', new_list, key='sector_box_1')

if sector_box == 'overall':
    fig4 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK price Range')
    st.plotly_chart(fig4, use_container_width=True)
else:
    temp_df = new_df[new_df['sector'] == sector_box]
    temp_df = temp_df[temp_df['bedRoom'] <= 4]
    fig4 = px.box(temp_df, x='bedRoom', y='price', title='BHK price Range')
    st.plotly_chart(fig4, use_container_width=True)

st.header('Side By Side Distribution plot for Property Type :')

# House
house_prices = new_df[new_df['property_type'] == 'house']['price']
house_kde = gaussian_kde(house_prices)
x_house = np.linspace(house_prices.min(), house_prices.max(), 200)
y_house = house_kde(x_house)

# Flat
flat_prices = new_df[new_df['property_type'] == 'flat']['price']
flat_kde = gaussian_kde(flat_prices)
x_flat = np.linspace(flat_prices.min(), flat_prices.max(), 200)
y_flat = flat_kde(x_flat)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_house, y=y_house, mode='lines', name='House'))
fig.add_trace(go.Scatter(x=x_flat, y=y_flat, mode='lines', name='Flat'))

fig.update_layout(title='Price Distribution: House vs Flat',
                  xaxis_title='Price', yaxis_title='Density')
st.plotly_chart(fig)




