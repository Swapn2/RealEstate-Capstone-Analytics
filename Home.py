# import streamlit as st
# st.set_page_config(
#      page_title = 'Hello',
#      page_icon = '$$',
#  )

# st.write('# welcome to stream lit :)>')
# # st.sidebar.success('select a demo')


import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI-Powered Real Estate Analytics",
    page_icon="🏡",
    layout="wide"
)

# -------------------- HEADER SECTION --------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: #2E86C1;
        text-align: center;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #555;
    }
    .highlight {
        background-color: #FDEDEC;
        padding: 8px 15px;
        border-radius: 8px;
        display: inline-block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>🏡 AI-Powered Real Estate Analytics & Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Leverage Data • Predict Prices • Explore Localities</p>", unsafe_allow_html=True)
st.write("---")


# -------------------- PROJECT OVERVIEW --------------------
st.markdown("## 📊 Project Overview")
st.markdown(
    """
    This platform helps **buyers, sellers, and investors** understand and predict real estate prices with ease.  
    Built with **Machine Learning, Web Scraping, and Interactive Dashboards**, it allows you to:
    
    - 📈 **Predict property prices** with up to **93% model accuracy** (MAE: 0.36).  
    - 🌎 **Explore spatial heatmaps** to visualize price variations across **20+ localities**.  
    - 🔎 Apply **interactive filters** to compare property features like size, locality, and price tiers.  
    - 🏷️ Identify **3 distinct pricing clusters** discovered using **KMeans clustering**.  
    - 🗂️ Benefit from an **automated web-scraping pipeline** that grew our dataset by **60%** using 5+ property portals.  
    """
)

st.write("---")


# -------------------- HIGHLIGHTED FEATURES --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📈 Model Accuracy", value="93%")
    st.caption("Trained on 10,000+ listings")

with col2:
    st.metric(label="📊 MAE", value="0.36")
    st.caption("Low error in price predictions")

with col3:
    st.metric(label="🌍 Localities Covered", value="20+")
    st.caption("Includes metro & suburban areas")

st.write("---")


# -------------------- CALL TO ACTION --------------------
st.markdown("## 🚀 Get Started")
st.info(
    "Use the sidebar to navigate to different sections:\n"
    "- **Price Prediction**: Enter property details to get an estimated price.\n"
    "- **Analytics Dashboard**: Explore trends, heatmaps, and filters.\n"
    "- **Locality Insights**: Understand pricing tiers and market patterns."
)

st.success("💡 Tip: Try adjusting the filters in the dashboard to reveal hidden trends in locality-wise pricing!")


# -------------------- FOOTER --------------------
st.write("---")
st.markdown(
    """
    <p style="text-align: center; color: #777;">
    Built with ❤️ using <b>Python • Streamlit • scikit-learn • BeautifulSoup</b>  
    <br>Deployed on <b>Streamlit Cloud</b> | © 2025 Real Estate Analytics
    </p>
    """,
    unsafe_allow_html=True
)
