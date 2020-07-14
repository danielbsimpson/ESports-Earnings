# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:32:20 2020

@author: Daniel Simpson
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "C:/Users/Damien/Desktop/Data Science Projects/ESports/datasets_Esports.csv",
    encoding = "ISO-8859-1")
sum_df = df.groupby('Year').agg({'Earnings' : 'sum',
                                 'Players' : 'sum',
                                 'Tournaments' : 'sum'}).reset_index()

def plot_totals(sum_df, value):
    plt.style.use('ggplot')
    x_values = sum_df['Year']
    y_values = sum_df[value]

    plt.ticklabel_format(style='plain')
    if value == 'Earnings':
        color = 'green'
        plt.title("ESports Total Tournament " + str(value))
        plt.ylabel(str(value) + " in USD")
    elif value == 'Players':
        color = 'blue'
        plt.title("ESports Total Tournament Participants")
        plt.ylabel("Number of " + str(value))
    else:
        color = 'red'
        plt.title("ESports Total Number of Tournaments")
        plt.ylabel("Number of " + str(value))
    plt.bar(x_values, y_values, color= color)            
    plt.xlabel("Years")

    return plt.show()

df_2020 = df[df['Year'] == 2020]    
df_2019 = df[df['Year'] == 2019]
df_2018 = df[df['Year'] == 2018]
df_2017 = df[df['Year'] == 2017]
df_2016 = df[df['Year'] == 2016]
df_2015 = df[df['Year'] == 2015]
df_2014 = df[df['Year'] == 2014]
df_2013 = df[df['Year'] == 2013]
df_2012 = df[df['Year'] == 2012]
df_2011 = df[df['Year'] == 2011]
df_2010 = df[df['Year'] == 2010]
df_2009 = df[df['Year'] == 2009]
df_2008 = df[df['Year'] == 2008]
df_2007 = df[df['Year'] == 2007]
df_2006 = df[df['Year'] == 2006]
df_2005 = df[df['Year'] == 2005]
df_2004 = df[df['Year'] == 2004]
df_2003 = df[df['Year'] == 2003]
df_2002 = df[df['Year'] == 2002]
df_2001 = df[df['Year'] == 2001]
df_2000 = df[df['Year'] == 2000]
df_1999 = df[df['Year'] == 1999]

df_list = [df_1999, df_2000, df_2001, df_2002, df_2003, df_2004, df_2005, 
           df_2006, df_2007, df_2008, df_2009, df_2010, df_2011, df_2012, 
           df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019,
           df_2020]

genre_list = []
for i in df_list:
    genre_list.append(
        i.groupby(['Year',
                   'Genre']).agg({'Earnings' : 'sum', 
                                  'Players' : 'sum', 
                                  'Tournaments' : 'sum'}
                                  ).reset_index().sort_values(
                                      by = ["Earnings"]))
#less than 10 genres had tournaments up until 2015
#so we will fill in 0 values for those years
#Thus our barchart race will be even throughout the years
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Puzzle Game', 
                                      'Earnings' : 0, 'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Role-Playing Game', 
                                      'Earnings' : 0, 'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Third-Person Shooter', 
                                      'Earnings' : 0, 'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Racing', 
                                      'Earnings' : 0, 
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Fighting Game', 
                                      'Earnings' : 0, 
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Sports', 
                                      'Earnings' : 0, 
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Collectible Card Game', 
                                      'Earnings' : 0, 
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Multiplayer Online Battle Arena', 
                                      'Earnings' : 0, 
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[0] = genre_list[0].append({'Year' : '1999', 
                                      'Genre' : 'Battle Royale', 
                                      'Earnings' : 0, 
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[1] = genre_list[1].append({'Year' : '2000',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[1] = genre_list[1].append({'Year' : '2000',
                                      'Genre' : 'Role-Playing Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[1] = genre_list[1].append({'Year' : '2000',
                                      'Genre' : 'Third-Person Shooter',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[1] = genre_list[1].append({'Year' : '2000',
                                      'Genre' : 'Racing',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[1] = genre_list[1].append({'Year' : '2000',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[1] = genre_list[1].append({'Year' : '2000',
                                      'Genre' : 'Multiplayer Online Battle Arena',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[1] = genre_list[1].append({'Year' : '2000',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[2] = genre_list[2].append({'Year' : '2001',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[2] = genre_list[2].append({'Year' : '2001',
                                      'Genre' : 'Role-Playing Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[2] = genre_list[2].append({'Year' : '2001',
                                      'Genre' : 'Third-Person Shooter',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[2] = genre_list[2].append({'Year' : '2001',
                                      'Genre' : 'Racing',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[2] = genre_list[2].append({'Year' : '2001',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[2] = genre_list[2].append({'Year' : '2001',
                                      'Genre' : 'Multiplayer Online Battle Arena',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[2] = genre_list[2].append({'Year' : '2001',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[3] = genre_list[3].append({'Year' : '2002',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[3] = genre_list[3].append({'Year' : '2002',
                                      'Genre' : 'Role-Playing Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[3] = genre_list[3].append({'Year' : '2002',
                                      'Genre' : 'Third-Person Shooter',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[3] = genre_list[3].append({'Year' : '2002',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[3] = genre_list[3].append({'Year' : '2002',
                                      'Genre' : 'Multiplayer Online Battle Arena',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[3] = genre_list[3].append({'Year' : '2002',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[4] = genre_list[4].append({'Year' : '2003',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[4] = genre_list[4].append({'Year' : '2003',
                                      'Genre' : 'Role-Playing Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[4] = genre_list[4].append({'Year' : '2003',
                                      'Genre' : 'Third-Person Shooter',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[4] = genre_list[4].append({'Year' : '2003', 
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[4] = genre_list[4].append({'Year' : '2003',
                                      'Genre' : 'Multiplayer Online Battle Arena',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[4] = genre_list[4].append({'Year' : '2003',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[5] = genre_list[5].append({'Year' : '2004',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[5] = genre_list[5].append({'Year' : '2004',
                                      'Genre' : 'Role-Playing Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[5] = genre_list[5].append({'Year' : '2004',
                                      'Genre' : 'Third-Person Shooter',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[5] = genre_list[5].append({'Year' : '2004',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[5] = genre_list[5].append({'Year' : '2004',
                                      'Genre' : 'Multiplayer Online Battle Arena',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[5] = genre_list[5].append({'Year' : '2004',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0, 
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[6] = genre_list[6].append({'Year' : '2005',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[6] = genre_list[6].append({'Year' : '2005',
                                      'Genre' : 'Role-Playing Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[6] = genre_list[6].append({'Year' : '2005',
                                      'Genre' : 'Third-Person Shooter',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[6] = genre_list[6].append({'Year' : '2005',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[6] = genre_list[6].append({'Year' : '2005',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[7] = genre_list[7].append({'Year' : '2006',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[7] = genre_list[7].append({'Year' : '2006',
                                      'Genre' : 'Role-Playing Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[7] = genre_list[7].append({'Year' : '2006',
                                      'Genre' : 'Third-Person Shooter',
                                      'Earnings' : 0, 
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[7] = genre_list[7].append({'Year' : '2006',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[7] = genre_list[7].append({'Year' : '2006',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[8] = genre_list[8].append({'Year' : '2007',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[8] = genre_list[8].append({'Year' : '2007',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[8] = genre_list[8].append({'Year' : '2007',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[9] = genre_list[9].append({'Year' : '2008',
                                      'Genre' : 'Puzzle Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[9] = genre_list[9].append({'Year' : '2008',
                                      'Genre' : 'Collectible Card Game',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[9] = genre_list[9].append({'Year' : '2008',
                                      'Genre' : 'Battle Royale',
                                      'Earnings' : 0,
                                      'Players' : 0,
                                      'Tournaments' : 0}, ignore_index = True)
genre_list[10] = genre_list[10].append({'Year' : '2009',
                                        'Genre' : 'Battle Royale',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[11] = genre_list[11].append({'Year' : '2010',
                                        'Genre' : 'Battle Royale',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[11] = genre_list[11].append({'Year' : '2010',
                                        'Genre' : 'Puzzle Game',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[12] = genre_list[12].append({'Year' : '2011',
                                        'Genre' : 'Battle Royale',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[12] = genre_list[12].append({'Year' : '2011',
                                        'Genre' : 'Puzzle Game',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[13] = genre_list[13].append({'Year' : '2012',
                                        'Genre' : 'Puzzle Game',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[13] = genre_list[13].append({'Year' : '2012',
                                        'Genre' : 'Collectible Card Game',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[13] = genre_list[13].append({'Year' : '2012',
                                        'Genre' : 'Battle Royale',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[14] = genre_list[14].append({'Year' : '2013',
                                        'Genre' : 'Puzzle Game',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[14] = genre_list[14].append({'Year' : '2013',
                                        'Genre' : 'Third-Person Shooter',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[14] = genre_list[14].append({'Year' : '2013',
                                        'Genre' : 'Battle Royale',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[15] = genre_list[15].append({'Year' : '2014',
                                        'Genre' : 'Puzzle Game',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[15] = genre_list[15].append({'Year' : '2014',
                                        'Genre' : 'Third-Person Shooter',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)
genre_list[15] = genre_list[15].append({'Year' : '2014',
                                        'Genre' : 'Battle Royale',
                                        'Earnings' : 0,
                                        'Players' : 0,
                                        'Tournaments' : 0}, ignore_index = True)

for i in range(0, len(genre_list)):
    genre_list[i] = genre_list[i].sort_values(by = 'Earnings',
                                              ascending = False)
    
color_list = ['#7e1e9c', '#15b01a', '#0343df', '#ff81c0', '#653700', '#e50000',
              '#95d0fc', '#029386', '#f97306', '#96f97b', '#c20078']

#Assign each genre equal to a specific color
genres = genre_list[0].Genre.values
genre_color = dict(zip(genres, color_list))

#function to plot the bar chart for each year
def genres_plot(game):
    game = game[::-1]
    genres = list(game.Genre.values)
    fig, ax = plt.subplots(figsize=(15, 8))

    ax.barh(genres, game['Earnings'], color=[genre_color[x] for x in genres])
    for i, (value, name) in enumerate(zip(game['Earnings'], genres)):
        ax.text(value, i,     name,size=18, weight=600, ha='left', va='bottom')
        ax.text(value, i -.25, f'{value:,.0f}',  size=14, ha='right',  va='center')
    
    ax.text(0, 1.12, 'Total Tournament Earnings per Genre',
        transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.text(1, 0.4, game['Year'][0], transform=ax.transAxes, size=46, ha='right')
    ax.set_axisbelow(True)
#Plot all the barcharts to be stitched together for a gif (BarChart Race)
def plot_all():    
    for i in range(0, len(genre_list)):
        genres_plot(genre_list[i])

#Plot top 10 games with highest tournament values
#Values is either 'Tournaments', 'Earnings', or 'Players'
#for number of tournaments, total prize earnings, or total number of
#participants in all tournaments in that game.
def plot_top10_games(df, value):    
    top10_tour = df.nlargest(10, value)

    plt.style.use('ggplot')
    x_values = top10_tour['Game']
    y_values = top10_tour[value]
    plt.bar(x_values, y_values, color=[genre_color[x] for x in top10_tour.Genre])
    plt.xticks(rotation=90)
    plt.ticklabel_format(style='plain', axis = 'y')
    if value == 'Earnings':
        plt.title("ESports Total Earnings by Game (" 
                  + str(list(df.Year)[0]) + ")")
        plt.ylabel("Tournament Earnings")
    elif value == 'Tournaments':
        plt.title("ESports Total Number of Tournaments by Game (" 
                  + str(list(df.Year)[0]) + ")")
        plt.ylabel("Number of Tournaments")
    elif value == 'Players':
        plt.title("ESports Total Number of Tournament Participants (" 
                  + str(list(df.Year)[0]) + ")")
        plt.ylabel("Number of Players in Tournaments")        
    plt.xlabel("Game Title")
    plt.show()
    
def plot_top10_all(value): #value = 'Earnings', 'Players', or 'Tournaments'
    for i in range(0, len(df_list)):
        plot_top10_games(df_list[i], value)