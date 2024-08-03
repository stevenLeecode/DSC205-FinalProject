import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv
player_total = pd.read_csv('Player Totals.csv')

st.title('NBA Greatest of All Time Comparisons')
st.subheader('Dataset: https://www.kaggle.com/datasets/rodneycarroll78/nba-stats-1980-2024?select=Player+Season+Info.csv ')

st.dataframe(player_total, width = 600, height = 200)
