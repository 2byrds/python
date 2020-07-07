import sys
import pandas as pd
import os

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 400)
pd.set_option('max_rows', 999)
import numpy as np

def main ():
    print(os.getcwd())

#    d = {'col1':[1,2], 'col2':[3,4]}
    roster = {'name':['aaron','brady','calvin'],'team':['A','B','C'],'position':['qb','qb','wr']}
    rdf = pd.DataFrame(roster)
    games = {'week':[1,1,2,2],'home_team':['A','C','E','G'],'away_team':['B','D','F','H']}
    gdf = pd.DataFrame(games) 
    
    qb_week1 = loadPositionWeek(rdf,gdf,'qb',1)
    
    
#    qb.append(rdf.loc[(rdf('team').isin(games['home_team'],games['away_team']) and rdf['position'] == 'qb')])

#df['stadium'] = df.apply(lambda df: get_stadium(df['team'],df['home_team']),axis=1)
#print(df)

def loadPositionWeek(rdf,gdf,position,week):
    print("roster:\n" + str(rdf))
    print("games:\n" + str(gdf))
    gdf_week = gdf[gdf.week == week]
    print("gdf week:\n" + str(gdf_week))
    rdf_position = rdf[rdf.position == position]
    print("rdf position:\n" + str(rdf_position))
    p_week = rdf_position.assign(stadium=lambda x:get_stadium(gdf_week,x.team))
    print("week " + str(week) + " " + str(position) + "s are:\n" + str(p_week))
    return p_week

def get_stadium(game_week,roster_position):
    stadium = 'bye'
    print("roster position:\n"+str(roster_position))
    
    print("position team\n" + str(pos_team))
    if(~game_week.loc[(game_week['home_team'] == pos_team)].empty):
        print("home player:\n" + str(game_week.loc[(game_week['home_team'] == pos_team)]))
        stadium = 'home'
    elif(~game_week.loc[(game_week['away_team'] == pos_team)].empty):
        print("away player:\n" + str(game_week.loc[(game_week['away_team'] == pos_team)]))
        stadium = 'away'
    print('stadium is:\n'+str(pd.Series(stadium, index=None)))
    return pd.Series(stadium, index=None)


if __name__ == "__main__":
    main()