import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv
player_total = pd.read_csv('Player Totals.csv')

st.title('NBA Greatest of All Time Comparisons - Steven Lee')
st.subheader('NBA Players Dataset')

st.dataframe(player_total, width = 800, height = 200)

# --- Question 1 ---

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

# --- Question 2 ---

#Gather player data to eventually plot
lbj = player_total[player_total['player'] == 'LeBron James']
lbj = lbj.loc[:, ['season', 'pts']]
lbj = lbj.sort_values(by = ['season'], ascending = True)
lbj = lbj.reset_index(drop=True)

mj = player_total[player_total['player'] == 'Michael Jordan']
mj = mj.loc[:, ['season', 'pts']]
mj = mj.sort_values(by = ['season'], ascending = True)
mj = mj.reset_index(drop=True)

kareem = player_total[player_total['player'] == 'Kareem Abdul-Jabbar']
kareem = kareem.loc[:, ['season', 'pts']]
kareem = kareem.sort_values(by = ['season'], ascending = True)
kareem = kareem.reset_index(drop=True)

curry = player_total[player_total['player'] == 'Stephen Curry']
curry = curry.loc[:, ['season', 'pts']]
curry = curry.sort_values(by = ['season'], ascending = True)
curry = curry.reset_index(drop=True)

kobe = player_total[player_total['player'] == 'Kobe Bryant']
kobe = kobe.loc[:, ['season', 'pts']]
kobe = kobe.sort_values(by = ['season'], ascending = True)
kobe = kobe.reset_index(drop=True)

#Plot

labels = ['Y' + str(i) for i in range(1, 22)]
print(labels)

fig = plt.figure(figsize = (16, 8))
ax = fig.add_subplot()
ax.set_xticks(lbj.index)
ax.set_xticklabels(labels)
ax.set_xlabel('Nth Year')
ax.set_ylabel('Points')
ax.set_title('Total Scoring each year for each player.')

'''
Color code for each player:

LeBron - Gold
Michael Jordan - red
Kareem - green
kobe - blue
steph curry - purple
'''


ax.plot(lbj.index, lbj['pts'], label = 'LeBron James', color = 'gold')
ax.plot(mj.index, mj['pts'], label = 'Michael Jordan', color = 'red')
ax.plot(kareem.index, kareem['pts'], label = 'Kareem Abdul-Jabbar', color = 'green')
ax.plot(curry.index, curry['pts'], label = 'Stephen Curry', color = 'purple')
ax.plot(kobe.index, kobe['pts'], label = 'Kobe Bryant', color = 'blue')

#Get top scoring seasons index to plot on scatter
lbj_max = lbj['pts'].idxmax()
mj_max = mj['pts'].idxmax()
kareem_max = kareem['pts'].idxmax()
curry_max = curry['pts'].idxmax()
kobe_max = kobe['pts'].idxmax()

# Plot the top scoring year as a dot
ax.scatter(lbj_max, lbj['pts'].max(), color='gold', zorder=5, s = 90, marker = '.')
ax.scatter(mj_max, mj['pts'].max(), color='red', zorder=5, s = 90, marker = '.')
ax.scatter(kareem_max, kareem['pts'].max(), color='green', zorder=5, s = 90, marker = '.')
ax.scatter(curry_max, curry['pts'].max(), color='purple', zorder=5, s = 90, marker = '.')
ax.scatter(kobe_max, kobe['pts'].max(), color='blue', zorder=5, s = 90, marker = '.')

#Annotate names directly on top of each point
ax.annotate('LeBron James ({lbj_max_pts})'.format(lbj_max_pts = lbj['pts'].max()), xy=(lbj_max, lbj['pts'].max()), xytext=(lbj_max - 0.7, lbj['pts'].max() + 50), color = 'gold')
ax.annotate('Michael Jordan ({mj_max_pts})'.format(mj_max_pts = mj['pts'].max()), xy=(mj_max, mj['pts'].max()), xytext=(mj_max - 0.76, mj['pts'].max() + 50), color = 'red')
ax.annotate('Kareem Abdul-Jabbar ({kareem_max_pts})'.format(kareem_max_pts = kareem['pts'].max()), xy=(kareem_max, kareem['pts'].max()), xytext=(kareem_max - 1, kareem['pts'].max() + 50), color = 'green')
ax.annotate('Stephen Curry ({curry_max_pts})'.format(curry_max_pts = curry['pts'].max()), xy=(curry_max, curry['pts'].max()), xytext=(curry_max - 0.775, curry['pts'].max() + 50), color = 'purple', zorder = 5)
ax.annotate('Kobe Bryant ({kobe_max_pts})'.format(kobe_max_pts = kobe['pts'].max()), xy=(kobe_max, kobe['pts'].max()), xytext=(kobe_max - 0.65, kobe['pts'].max() + 50), color = 'blue')


ax.legend(fancybox = True, framealpha = 1, shadow = True, borderpad = 1)

st.pyplot(fig = fig, clear_figure = True)