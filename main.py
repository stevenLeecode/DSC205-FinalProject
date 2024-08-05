import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Entry Point",
    page_icon="🏆",
)

st.sidebar.success("Main")

#https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv
player_total = pd.read_csv('Player Totals.csv')

#st.title('NBA Greatest of All Time Comparisons - Steven Lee')
st.markdown("<h2 style = 'text-align: center'> NBA Greatest Player of All Time Comparisons <h2>", unsafe_allow_html=True)
st.markdown("<h3 style = 'text-align: center'> NBA Players Dataset </h3>", unsafe_allow_html=True)

st.dataframe(player_total, width = 1400, height = 275)

# --- Question 1 ---
st.markdown('---')
st.markdown("<h3 style = 'text-align: center'> Each Players first 3 years </h3>", unsafe_allow_html=True)
#Get lebrons pts for the his first 3 seasons into a dataframe.
#Rookie season was 2003, so include seasons 04', 05', 06'.
lbj = player_total[(player_total['player'] == 'LeBron James') & (player_total['season'] < 2007)]

lbj_1 = lbj.loc[:, ['season', 'pts', 'mp']]
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
mj = mj.loc[:, ['season', 'pts', 'mp']]
mj = mj[mj['season'] <= 1987]
mj = mj.sort_values(by = ['season'], ascending = True)
mj = mj.reset_index(drop=True)

#Get Kareems pts for his first 3 seasons into a dataframe.
#Rookie season was 1969, so include seasons 70', 71', 72'.
kareem = player_total[player_total['player'] == 'Kareem Abdul-Jabbar']
kareem = kareem.loc[:, ['season', 'pts', 'mp']]
kareem = kareem[kareem['season'] <= 1972]
kareem = kareem.sort_values(by = ['season'], ascending = True)
kareem = kareem.reset_index(drop=True)

#Get Kobe's pts for his first 3 seasons into a dataframe.
#Rookie season was 1996, so include seasons 97', 98', 99'.

kobe = player_total[player_total['player'] == 'Kobe Bryant']
kobe = kobe.loc[:,['season', 'pts', 'mp']]
kobe = kobe[kobe['season'] <= 1999]
kobe = kobe.sort_values(by = ['season'], ascending = True)
kobe = kobe.reset_index(drop=True)

#Get Curry's pts for his first 3 seasons into a dataframe.
#Rookie season was 2009, so include seasons 10', 11', 12'

curry = player_total[player_total['player'] == 'Stephen Curry']
curry = curry.loc[:,['season', 'pts', 'mp']]
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


ax.annotate(f'LeBron James ({lbj_1["mp"][0]} mins played)', xy=(lbj_1.index[0], lbj_1['pts'][0]), xytext=(lbj_1.index[0], lbj_1['pts'][0] - 75), color = 'gold')
ax.annotate(f'Michael Jordan ({mj["mp"][0]} mins played)', xy=(mj.index[0], mj['pts'][0]), xytext=(mj.index[0] + 0.1, mj['pts'][0] - 75), color = 'red')
ax.annotate(f'Kareem Abdul-Jabbar ({kareem["mp"][0]} mins played)', xy=(kareem.index[0], kareem['pts'][0]), xytext=(kareem.index[0], kareem['pts'][0] + 125), color = 'green')
ax.annotate(f'Kobe Bryant ({kobe["mp"][0]} mins played)', xy=(kobe.index[0], kobe['pts'][0]), xytext=(kobe.index[0], kobe['pts'][0] - 100), color = 'blue')
ax.annotate(f'Stephen Curry ({curry["mp"][0]} mins played)', xy=(curry.index[0], curry['pts'][0]), xytext=(curry.index[0], curry['pts'][0] - 100), color = 'purple')

st.pyplot(fig = fig, clear_figure = True)

st.markdown("<h3 style = 'text-align: center'> Each Players last 3 years </h3>", unsafe_allow_html=True)

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot()
ax.set_xlabel('Year')
ax.set_ylabel('Points')
ax.set_title('Total Points Scored for Last Three Years played in NBA')
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['Third Last Year', 'Second Last Year', 'Retirement / Last Year'])

def last_3_seasons(player, last_season_less_3, player_color):
    player = player_total[player_total['player'] == player]
    player = player.loc[:, ['player','season', 'pts', 'mp']]
    player = player[player['season'] >= last_season_less_3]
    player = player.sort_values(by = ['season'], ascending = True)
    player = player.reset_index(drop=True)
    player_name = player['player'][0]

    ax.plot(player.index, player['pts'], label = player_name, color = player_color)
    if player_name == 'Kareem Abdul-Jabbar':
        ax.annotate(f'{player_name} ({player["mp"][0]} mins played)', xy=(player.index[0], player['pts'][0]), xytext=(player.index[0], player['pts'][0] - 195), color = player_color)
    elif player_name == 'Stephen Curry':
        ax.annotate(f'{player_name} ({player["mp"][0]} mins played)', xy=(player.index[0], player['pts'][0]), xytext=(player.index[0], player['pts'][0] - 100), color = player_color)
    elif player_name == 'Kobe Bryant' or player_name == 'Michael Jordan':
        ax.annotate(f'{player_name} ({player["mp"][0]} mins played)', xy=(player.index[0], player['pts'][0]), xytext=(player.index[0] + 0.1, player['pts'][0]), color = player_color)
    else:
        ax.annotate(f'{player_name} ({player["mp"][0]} mins played)', xy=(player.index[0], player['pts'][0]), xytext=(player.index[0], player['pts'][0] + 35), color = player_color)
    ax.legend()

player_goats = (['LeBron James', 2022, 'gold'], ['Michael Jordan', 1998, 'red'], ['Kareem Abdul-Jabbar', 1987, 'green'],
    ['Kobe Bryant', 2014, 'blue'], ['Stephen Curry', 2022, 'purple'])

for name, year, p_color in player_goats:
    last_3_seasons(name, year, p_color)



st.pyplot(fig = fig, clear_figure = True)


# --- Question 2 ---
st.markdown('---')
st.subheader('Total Scoring for each player per year in league')
#Gather player data to eventually plot
def get_scoring_data(player):
  player = player_total[player_total['player'] == player]
  player = player.loc[:, ['player','season', 'pts']]
  player = player.sort_values(by = ['season'], ascending = True)
  player = player.reset_index(drop=True)
  return player

lbj_scoring = get_scoring_data('LeBron James')
mj_scoring = get_scoring_data('Michael Jordan')
kareem_scoring = get_scoring_data('Kareem Abdul-Jabbar')
kobe_scoring = get_scoring_data('Kobe Bryant')
curry_scoring = get_scoring_data('Stephen Curry')

#Plot
#Plotting
labels = ['Y' + str(i) for i in range(1, 22)]

fig = plt.figure(figsize = (16, 8))
ax = fig.add_subplot()
ax.set_xlabel('Season')
ax.set_xticks(lbj_scoring.index) #LeBron has longest season out of all players
ax.set_xticklabels(labels)
ax.set_ylabel('Points')
ax.set_title('Total Scoring each season for each player')

def chart_total_scoring(player, figure, line_color):
  ax.plot(player.index, player['pts'], label = player['player'][0], color = line_color)
  ax.scatter(player['pts'].idxmax(), player['pts'].max(), color=line_color, zorder=5, s = 60, marker = '.') #Put dot on max scoring point
  ax.legend()

curry_scoring_chart = chart_total_scoring(curry_scoring, fig, 'purple')
lbj_scoring_chart = chart_total_scoring(lbj_scoring, fig, 'gold')
mj_scoring_chart = chart_total_scoring(mj_scoring, fig, 'red')
kareem_scoring_chart = chart_total_scoring(kareem_scoring, fig, 'green')
kobe_scoring_chart = chart_total_scoring(kobe_scoring, fig, 'blue')

lbj_max = lbj_scoring['pts'].idxmax()
mj_max = mj_scoring['pts'].idxmax()
kareem_max = kareem_scoring['pts'].idxmax()
curry_max = curry_scoring['pts'].idxmax()
kobe_max = kobe_scoring['pts'].idxmax()

#Annotate names directly on top of each point
ax.annotate('LeBron James ({lbj_max_pts} pts)'.format(lbj_max_pts = lbj_scoring['pts'].max()), xy=(lbj_max, lbj_scoring['pts'].max()), xytext=(lbj_max - 0.7, lbj_scoring['pts'].max() + 50), color = 'gold')
ax.annotate('Michael Jordan ({mj_max_pts} pts)'.format(mj_max_pts = mj_scoring['pts'].max()), xy=(mj_max, mj_scoring['pts'].max()), xytext=(mj_max - 0.76, mj_scoring['pts'].max() + 50), color = 'red')
ax.annotate('Kareem Abdul-Jabbar ({kareem_max_pts} pts)'.format(kareem_max_pts = kareem_scoring['pts'].max()), xy=(kareem_max, kareem_scoring['pts'].max()), xytext=(kareem_max - 1, kareem_scoring['pts'].max() + 50), color = 'green')
ax.annotate('Stephen Curry ({curry_max_pts} pts)'.format(curry_max_pts = curry_scoring['pts'].max()), xy=(curry_max, curry_scoring['pts'].max()), xytext=(curry_max - 0.775, curry_scoring['pts'].max() + 50), color = 'purple', zorder = 10)
ax.annotate('Kobe Bryant ({kobe_max_pts} pts)'.format(kobe_max_pts = kobe_scoring['pts'].max()), xy=(kobe_max, kobe_scoring['pts'].max()), xytext=(kobe_max - 0.65, kobe_scoring['pts'].max() + 50), color = 'blue')

st.pyplot(fig = fig, clear_figure = True)

goat_players = ['LeBron James', 'Michael Jordan', 'Kareem Abdul-Jabbar', 'Kobe Bryant', 'Stephen Curry']
#st.subheader('Select Players to plot their Points Scored per Year')

#for i in goat_players:
#    checkboxes = st.checkbox(i)


st.markdown('---')
st.subheader('Player Points Regression Plot')

# REG PLOT RADIO BTN

def plot_reg_plot(player):
  player_name = player['player'][0]
  fig = plt.figure(figsize = (16, 8))
  sns.regplot(x = player['season'], y = player['pts'], line_kws = {'color': 'red'}).set_title(f'{player_name} Total Points Per Season')
  plt.xticks(player['season'])
  #Show average value using axvline
  #ax.axhline(player['pts'].mean(), color='black', linestyle='dashed', linewidth=1)
  return st.pyplot(fig = fig, clear_figure = True)

player_input = st.radio('Select a Player', ('LeBron James', 'Michael Jordan', 'Kareem Abdul-Jabbar', 'Kobe Bryant', 'Stephen Curry'))

if player_input == 'LeBron James':
    plot_reg_plot(lbj_scoring)
elif player_input == 'Michael Jordan':
    plot_reg_plot(mj_scoring)
elif player_input == 'Kareem Abdul-Jabbar':
    plot_reg_plot(kareem_scoring)
elif player_input == 'Kobe Bryant':
    plot_reg_plot(kobe_scoring)
else:
    plot_reg_plot(curry_scoring)

st.markdown('---')
# --- Question 3 --- Assists

st.subheader('Assists comparison for each players career')
#Gather assist data from each players full career.

def assist_data(player):
  lbj = player_total[player_total['player'] == player]
  lbj = lbj.loc[:, ['season', 'ast']]
  lbj = lbj.sort_values(by = ['season'], ascending = True)
  lbj = lbj.reset_index(drop=True)
  return lbj

kareem_ast = assist_data('Kareem Abdul-Jabbar')
lebron_ast = assist_data('LeBron James')
kobe_ast = assist_data('Kobe Bryant')
curry_ast = assist_data('Stephen Curry')
mj_ast = assist_data('Michael Jordan')

labels = ['Y' + str(i) for i in range(1, 22)]
print(labels)

#Gather max assists from each player index to plot on X axis.

lebron_ast_max = lebron_ast['ast'].idxmax()
kareem_ast_max = kareem_ast['ast'].idxmax()
kobe_ast_max = kobe_ast['ast'].idxmax()
curry_ast_max = curry_ast['ast'].idxmax()
mj_ast_max = mj_ast['ast'].idxmax()

#Plot assist data.

fig = plt.figure(figsize = (16, 8))
ax = fig.add_subplot()
ax.set_xticks(lebron_ast.index) #LeBron / Kareem has longest playing career
ax.set_xticklabels(labels)
ax.set_xlabel('Nth Year')
ax.set_ylabel('Assists per season')
ax.set_title('Total Assists each year for each player.')

sns.lineplot(data = lebron_ast, x = lebron_ast.index, y = lebron_ast['ast'], label = 'LeBron James', color = 'gold')
sns.lineplot(data = kareem_ast, x = kareem_ast.index, y = kareem_ast['ast'], label = 'Kareem Abdul-Jabbar', color = 'green')
sns.lineplot(data = kobe_ast, x = kobe_ast.index, y = kobe_ast['ast'], label = 'Kobe Bryant', color = 'blue')
sns.lineplot(data = curry_ast, x = curry_ast.index, y = curry_ast['ast'], label = 'Stephen Curry', color = 'purple')
sns.lineplot(data = mj_ast, x = mj_ast.index, y = mj_ast['ast'], label = 'Michael Jordan', color = 'red')

ax.scatter(lebron_ast_max, lebron_ast['ast'].max(), color='gold', zorder=5, s = 90, marker = '.')
ax.scatter(kareem_ast_max, kareem_ast['ast'].max(), color='green', zorder=5, s = 90, marker = '.')
ax.scatter(kobe_ast_max, kobe_ast['ast'].max(), color='blue', zorder=5, s = 90, marker = '.')
ax.scatter(curry_ast_max, curry_ast['ast'].max(), color='purple', zorder=5, s = 90, marker = '.')
ax.scatter(mj_ast_max, mj_ast['ast'].max(), color='red', zorder=5, s = 90, marker = '.')

ax.annotate('LeBron James', xy=(lebron_ast_max, lebron_ast['ast'].max()), xytext=(lebron_ast_max - 0.73, lebron_ast['ast'].max() + 15), color = 'gold')
ax.annotate('Kareem Abdul-Jabbar', xy=(kareem_ast_max, kareem_ast['ast'].max()), xytext=(kareem_ast_max - 1, kareem_ast['ast'].max() + 15), color = 'green')
ax.annotate('Kobe Bryant', xy=(kobe_ast_max, kobe_ast['ast'].max()), xytext=(kobe_ast_max - 0.6, kobe_ast['ast'].max() + 15), color = 'blue')
ax.annotate('Stephen Curry', xy=(curry_ast_max, curry_ast['ast'].max()), xytext=(curry_ast_max - 0.7, curry_ast['ast'].max() + 15), color = 'purple')
ax.annotate('MJ', xy=(mj_ast_max, mj_ast['ast'].max()), xytext=(mj_ast_max - 0.1, mj_ast['ast'].max() - 45), color = 'red')

ax.legend()

st.pyplot(fig = fig, clear_figure = True)

# --- Question 4 --- Defensive/Offensive Rebounds
st.markdown('---')

def rebound_data(player):
  player_reb = player_total[player_total['player'] == player]
  player_reb = player_reb.loc[:, ['player','season', 'orb', 'drb']]
  player_reb = player_reb.sort_values(by = ['season'], ascending = True)
  player_reb = player_reb.reset_index(drop=True)
  return player_reb

lbj_reb = rebound_data('LeBron James')
mj_reb = rebound_data('Michael Jordan')
kareem_reb = rebound_data('Kareem Abdul-Jabbar')
kobe_reb = rebound_data('Kobe Bryant')
curry_reb = rebound_data('Stephen Curry')

def chart_rebounds(player):

  player_name = player['player'][0]

  fig = plt.figure(figsize = (16, 8))
  ax = fig.add_subplot()
  ax.set_xlabel('Season')
  ax.set_ylabel('Rebounds per Season')
  ax.set_title('Total Rebounds each season for {}.'.format(player_name))

  ax.set_xticks(player['season'])
  ax.plot(player['season'], player['drb'], label = 'Defensive Rebounds')
  ax.plot(player['season'], player['orb'], label = 'Offensive Rebounds')
  ax.legend()
  return st.pyplot(fig = fig, clear_figure = True)

st.subheader('Rebounds Plot (Defensive/Offensive)')
player_option_reb = st.selectbox('Select a Player', ('LeBron James', 'Michael Jordan', 'Kareem Abdul-Jabbar', 'Kobe Bryant', 'Stephen Curry'), key = 'reb_key')

if player_option_reb == 'LeBron James':
    chart_rebounds(lbj_reb)
elif player_option_reb == 'Michael Jordan':
    chart_rebounds(mj_reb)
elif player_option_reb == 'Kareem Abdul-Jabbar':
    chart_rebounds(kareem_reb)
elif player_option_reb == 'Kobe Bryant':
    chart_rebounds(kobe_reb)
else:
    chart_rebounds(curry_reb)

st.markdown('---')
# --- Question 5 --- Steals

def steal_data(player):
  player_stl = player_total[player_total['player'] == player]
  player_stl = player_stl.loc[:, ['player','season', 'stl']]
  player_stl = player_stl.sort_values(by = ['season'], ascending = True)
  player_stl = player_stl.reset_index(drop=True)
  return player_stl

lbj_stl = steal_data('LeBron James')
mj_stl = steal_data('Michael Jordan')
kareem_stl = steal_data('Kareem Abdul-Jabbar')
kobe_stl = steal_data('Kobe Bryant')
curry_stl = steal_data('Stephen Curry')

def chart_steals(player, player_color):
  player_name = player['player'][0]

  fig = plt.figure(figsize = (16, 8))
  ax = fig.add_subplot()
  ax.set_xlabel('Season')
  ax.set_ylabel('Steals per Season')
  ax.set_title('Total Steals each season for {}.'.format(player_name))

  ax.set_xticks(player['season'])
  ax.plot(player['season'], player['stl'], label = 'Steals per Season', color = player_color)
  ax.legend()
  return st.pyplot(fig = fig, clear_figure = True)


st.subheader('Steals Plot')
player_option_stl = st.selectbox('Select a Player', ('LeBron James', 'Michael Jordan', 'Kareem Abdul-Jabbar', 'Kobe Bryant', 'Stephen Curry'), key = 'stl_key')

if player_option_stl == 'LeBron James':
    chart_steals(lbj_stl, 'gold')
elif player_option_stl == 'Michael Jordan':
    chart_steals(mj_stl, 'green')
elif player_option_stl == 'Kareem Abdul-Jabbar':
    chart_steals(kareem_stl, 'purple')
elif player_option_stl == 'Kobe Bryant':
    chart_steals(kobe_stl, 'red')
else:
    chart_steals(curry_stl, 'blue')

def chart_steals_overlap(players):
    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot()
    ax.set_xlabel('Season')
    ax.set_ylabel('Steals per Season')
    ax.set_title('Total Steals each season for each player.')
    ax.set_xticks([1965, 1970, 1980, 1990, 2000, 2010, 2020])

    for player in players:
        player_name = player['player'][0]
        ax.plot(player['season'], player['stl'], label=player_name)

    ax.legend()
    return st.pyplot(fig = fig, clear_figure = True)

# Assuming curry_stl, lbj_stl, mj_stl, kobe_stl, and kareem_stl are already defined
players = [curry_stl, lbj_stl, mj_stl, kobe_stl, kareem_stl]
chart_steals_overlap(players)

# --- Question 6 --- Blocks
st.markdown('---')
st.markdown("<h3 style = 'text-align: center'> Compare total blocks per each players season. </h3>", unsafe_allow_html=True)

def block_data(player):
  player_stl = player_total[player_total['player'] == player]
  player_stl = player_stl.loc[:, ['player','season', 'blk']]
  player_stl = player_stl.sort_values(by = ['season'], ascending = True)
  player_stl = player_stl.reset_index(drop=True)
  return player_stl

lbj_blk = block_data('LeBron James')
mj_blk = block_data('Michael Jordan')
kareem_blk = block_data('Kareem Abdul-Jabbar')
kobe_blk = block_data('Kobe Bryant')
curry_blk = block_data('Stephen Curry')

#Kareem is missing 4 values
kareem_blk.isna().sum().sum()
kareem_blk_no_NaN = kareem_blk.dropna()
kareem_blk_no_NaN.reset_index(drop=True, inplace=True) #Reset index to grab players name

def chart_blocks(player):

  player_name = player['player'][0]

  fig = plt.figure(figsize = (16, 8))
  ax = fig.add_subplot()
  ax.set_xlabel('Season')
  ax.set_ylabel('blocks per Season')
  ax.set_title('Total blocks each season for {}.'.format(player_name))

  ax.set_xticks(player['season'])
  plot = ax.plot(player['season'], player['blk'], label = 'Blocks per season')
  ax.legend()
  #return st.pyplot(fig = fig, clear_figure = True)
  return st.pyplot(fig = fig, clear_figure = True)


player_multiselect_blk = st.multiselect('Select two players to compare block statistics',
    ['LeBron James', 'Michael Jordan', 'Kobe Bryant', 'Kareem Abdul-Jabbar', 'Stephen Curry'], max_selections = 3)

col1, col2 = st.columns(2)

with col1:
    if len(player_multiselect_blk) == 2:
        if player_multiselect_blk[0] == 'LeBron James':
            chart_blocks(lbj_blk)
        elif player_multiselect_blk[0] == 'Michael Jordan':
            chart_blocks(mj_blk)
        elif player_multiselect_blk[0] == 'Kobe Bryant':
            chart_blocks(kobe_blk)
        elif player_multiselect_blk[0] == 'Kareem Abdul-Jabbar':
            chart_blocks(kareem_blk)
        else:
            chart_blocks(curry_blk)

with col2:
    if len(player_multiselect_blk) == 2:
        if player_multiselect_blk[1] == 'LeBron James':
            chart_blocks(lbj_blk)
        elif player_multiselect_blk[1] == 'Michael Jordan':
                chart_blocks(mj_blk)
        elif player_multiselect_blk[1] == 'Kobe Bryant':
            chart_blocks(kobe_blk)
        elif player_multiselect_blk[1] == 'Kareem Abdul-Jabbar':
            chart_blocks(kareem_blk)
        else:
            chart_blocks(curry_blk)