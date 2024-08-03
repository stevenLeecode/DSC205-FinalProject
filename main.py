import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv
player_total = pd.read_csv('Player Totals.csv')

st.title('NBA Greatest of All Time Comparisons - Steven Lee')
st.subheader('NBA Players Dataset')

st.dataframe(player_total, width = 600, height = 200)
