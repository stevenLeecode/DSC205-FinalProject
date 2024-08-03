import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


player_total = pd.read_csv('https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv')

st.title('NBA Greatest of All Time Comparisons')
st.subheader('LeBron James, Michael Jordan, Kareem Abdul-Jabbar, Kobe Bryant, Stephen Curry')
