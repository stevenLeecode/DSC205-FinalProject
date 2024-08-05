import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Defensive Stats",
    page_icon = '🏀'
)


#https://raw.githubusercontent.com/stevenLeecode/DSC205-FinalProject/main/Player%20Totals.csv
player_total = pd.read_csv('..\Player Totals.csv')

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