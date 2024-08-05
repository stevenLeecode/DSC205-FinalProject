import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Homepage"
)

st.sidebar.success("Welcome to my DSC Project - Steven Lee")

#https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv
player_total = pd.read_csv('Player Totals.csv')

#st.title('NBA Greatest of All Time Comparisons - Steven Lee')
st.markdown("<h2 style = 'text-align: center'> NBA Greatest Player of All Time Comparisons <h2>", unsafe_allow_html=True)
st.markdown("<h3 style = 'text-align: center'> NBA Players Dataset </h3>", unsafe_allow_html=True)

st.dataframe(player_total, width = 1400, height = 275)

subheader_link_html = """
<h3 style = 'text-align: center;'> Kaggle Dataset <a href = https://www.kaggle.com/datasets/rodneycarroll78/nba-stats-1980-2024?select=Player+Season+Info.csv> Link </a> </h3>
"""

st.markdown(subheader_link_html, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image('dsc205-streamlit-nbapics/jordan.jpg', caption = 'Michael Jordan')

with col3:
    st.image('dsc205-streamlit-nbapics/kareem.jpg', caption = 'Michael Jordan')

with col5:
    st.image('dsc205-streamlit-nbapics/curry.jpg', caption = 'Michael Jordan')