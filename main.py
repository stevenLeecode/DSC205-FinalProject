import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv
player_total = pd.read_csv('Player Totals.csv')

st.title('NBA Greatest of All Time Comparisons - Steven Lee')
st.subheader('NBA Players Dataset')

st.dataframe(player_total, width = 800, height = 200)

#Get lebrons pts for the his first 3 seasons into a dataframe.
#Rookie season was 2003, so include seasons 04', 05', 06'.
lbj = player_total[(player_total['player'] == 'LeBron James') & (player_total['season'] < 2007)]

lbj_1 = lbj.loc[:, ['season', 'pts']]
lbj_1 = lbj_1.sort_values(by = ['season'], ascending = True)
lbj_1 = lbj_1.reset_index(drop=True)
#drop season column
lbj_1 = lbj_1.drop(columns=['season'])
#lbj_1 = lbj_1[::-1].reset_index(drop=True)

#Plot LeBron's total points for first 3 seasons.
#Test for future plots.

labels = ['Year 1', 'Year 2', 'Year 3'] #Labels for X axis

#Get MJ's pts for the his first 3 seasons into a dataframe.
#Rookie season was 1984, so include seasons 85', 86', 87'.
mj = player_total[player_total['player'] == 'Michael Jordan']
mj = mj.loc[:, ['season', 'pts']]
mj = mj[mj['season'] <= 1987]
mj = mj.sort_values(by = ['season'], ascending = True)
mj = mj.reset_index(drop=True)

#Get Kareems pts for his first 3 seasons into a dataframe.
#Rookie season was 1969, so include seasons 70', 71', 72'.
kareem = player_total[player_total['player'] == 'Kareem Abdul-Jabbar']
kareem = kareem.loc[:, ['season', 'pts']]
kareem = kareem[kareem['season'] <= 1972]
kareem = kareem.sort_values(by = ['season'], ascending = True)
kareem = kareem.reset_index(drop=True)

#Get Kobe's pts for his first 3 seasons into a dataframe.
#Rookie season was 1996, so include seasons 97', 98', 99'.

kobe = player_total[player_total['player'] == 'Kobe Bryant']
kobe = kobe.loc[:,['season', 'pts']]
kobe = kobe[kobe['season'] <= 1999]
kobe = kobe.sort_values(by = ['season'], ascending = True)
kobe = kobe.reset_index(drop=True)

#Get Curry's pts for his first 3 seasons into a dataframe.
#Rookie season was 2009, so include seasons 10', 11', 12'

curry = player_total[player_total['player'] == 'Stephen Curry']
curry = curry.loc[:,['season', 'pts']]
curry = curry[curry['season'] <= 2012]
curry = curry.sort_values(by = ['season'], ascending = True)
curry = curry.reset_index(drop=True)

#Plot everyone.

labels = ['Season 1', 'Season 2', 'Season 3']
fig = plt.figure(figsize = (14, 8)) #figsize goes x, y dimensions.
ax = fig.add_subplot()
ax.set_xticks(lbj_1.index)
ax.set_xticklabels(labels)

ax.plot(lbj_1.index, lbj_1['pts'], label = 'LeBron James', color = 'gold')
ax.plot(mj.index, mj['pts'], label = 'Michael Jordan', color = 'red')
ax.plot(kareem.index, kareem['pts'], label = 'Kareem Abdul-Jabbar', color = 'green')
ax.plot(kobe.index, kobe['pts'], label = 'Kobe Bryant', color = 'blue')
ax.plot(curry.index, curry['pts'], label = 'Stephen Curry', color = 'purple')


ax.set_xlabel('Year')
ax.set_ylabel('Points')
ax.set_title('Total Points for First Three Years played in NBA')


ax.annotate('LeBron James', xy=(lbj_1.index[0], lbj_1['pts'][0]), xytext=(lbj_1.index[0], lbj_1['pts'][0] - 75), color = 'gold')
ax.annotate('Michael Jordan', xy=(mj.index[0], mj['pts'][0]), xytext=(mj.index[0] + 0.1, mj['pts'][0] - 75), color = 'red')
ax.annotate('Kareem Abdul-Jabbar', xy=(kareem.index[0], kareem['pts'][0]), xytext=(kareem.index[0], kareem['pts'][0] + 125), color = 'green')
ax.annotate('Kobe Bryant', xy=(kobe.index[0], kobe['pts'][0]), xytext=(kobe.index[0], kobe['pts'][0] - 100), color = 'blue')
ax.annotate('Stephen Curry', xy=(curry.index[0], curry['pts'][0]), xytext=(curry.index[0], curry['pts'][0] - 100), color = 'purple')

st.pyplot(fig = fig, clear_figure = True)