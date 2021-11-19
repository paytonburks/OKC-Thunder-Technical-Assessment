'''
Programmer: Payton Burks
11/19/2021
OKC Thunder Technical Assessment

Utility functions used for thunder.py; helps compute statistics as well as split team data
'''
import math

def is_three_pointer(x, y):
    '''
    determines if a shot (past +7.8 in the y direction) is a three pointer based on location

    parameters:
        x: x coordinate of a shot attempt
        y: y coordinate of a shot attempt
    '''
    hyp = math.sqrt(x**2 + y**2)
    if hyp > 23.75:
        return True
    return False

def efg (x):
    '''
    computes the effective field goal percent of a dataset

    parameters:
        x: dataframe of shot data
    '''
    makes = (x['fgmade'] == 1).sum()
    misses = (x['fgmade'] == 0).sum()

    if x['shotlocation'][0] == '2PT':
        efg = makes/(makes+misses)
    else:
        efg = 1.5*makes/(makes+misses)

    return round(efg, 8)

def shot_distr(two_p, nc_three, c_three):
    '''
    computes the shot distributions of two pointers, non-corner threes, and corner threes

    parameters:
        two_p: dataframe of two-point shot data
        nc_three: dataframe of non-corner three-point shot data
        c_three: dataframe of corner three-point shot data
    '''
    num_shots = len(two_p) + len(nc_three) + len(c_three)

    two_point_distr = len(two_p)/num_shots
    nc_three_distr = len(nc_three)/num_shots
    c_three_distr = len(c_three)/num_shots

    return round(two_point_distr, 8), round(nc_three_distr, 8), round(c_three_distr, 8)

def split_team_data(df):
    '''
    splits a dataframe by team A & team B

    parameters:
        df: dataframe of shot data
    '''
    group_by_team = df.groupby('team')
    team_data_list = []
    for group_name, group_df in group_by_team:
        group_df = group_df.drop(columns='index').reset_index().drop(columns='index')
        team_data_list.append(group_df)

    return team_data_list[0], team_data_list[1]
