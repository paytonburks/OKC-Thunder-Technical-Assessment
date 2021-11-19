'''
Programmer: Payton Burks
11/19/2021
OKC Thunder Technical Assessment 

Computes statistics from team shooting data
'''
import pandas as pd
import sys
import utils

def main():
    # import data from csv, put into pandas dataframe
    data = open('shots_data.csv', "r")
    df = pd.read_csv(data, header=0, index_col=None)

    # add 2PT, NC3, C3 info to a new series
    shot_area_ser = []
    for i in range(0, len(df['x']), 1):
        if (abs(df['x'][i]) <= 22 and df['y'][i] <= 7.8):
            shot_area_ser.append("2PT")
        elif (abs(df['x'][i]) > 22 and df['y'][i] <= 7.8):
            shot_area_ser.append("C3")
        else:
            if(utils.is_three_pointer(df['x'][i], df['y'][i])):
                shot_area_ser.append("NC3")
            else:
                shot_area_ser.append("2PT")

    # add series to dataframe
    df['shotlocation'] = shot_area_ser

    # split data points by shot location, get new dfs
    two_point_data = []
    nc_three_data = []
    c_three_data = []

    for i in range(0, len(df['shotlocation']), 1):
        if df['shotlocation'][i] == '2PT':
            two_point_data.append(df.iloc[i])
        elif df['shotlocation'][i] == 'C3':
            c_three_data.append(df.iloc[i])
        else:
            nc_three_data.append(df.iloc[i])

    two_point_df = pd.DataFrame(two_point_data).reset_index()
    nc_three_df = pd.DataFrame(nc_three_data).reset_index()
    c_three_df = pd.DataFrame(c_three_data).reset_index()

    # get data for team A and team B
    two_point_A, two_point_B = utils.split_team_data(two_point_df)
    nc_three_A, nc_three_B = utils.split_team_data(nc_three_df)
    c_three_A, c_three_B = utils.split_team_data(c_three_df)

    # shot distribution
    two_point_distr_A, nc_three_distr_A, c_three_distr_A = utils.shot_distr(two_point_A, nc_three_A, c_three_A)
    two_point_distr_B, nc_three_distr_B, c_three_distr_B = utils.shot_distr(two_point_B, nc_three_B, c_three_B)

    # efg
    efg_2pt_A = utils.efg(two_point_A)
    efg_nc_three_A = utils.efg(nc_three_A)
    efg_c_three_A = utils.efg(c_three_A)

    efg_2pt_B = utils.efg(two_point_B)
    efg_nc_three_B = utils.efg(nc_three_B)
    efg_c_three_B = utils.efg(c_three_B)

    # pretty print results to output.txt
    with open ('output.txt', 'w') as fout:
        sys.stdout = fout

        print("***** TEAM A *****\n")

        print("Shot Distributions: \n")
        print("2PT:", two_point_distr_A)
        print("NC3:", nc_three_distr_A)
        print("C3:", c_three_distr_A, '\n')

        print("Effective Field Goal Percentages: \n")
        print("2PT:", efg_2pt_A)
        print("NC3:", efg_nc_three_A)
        print("C3:", efg_c_three_A, "\n")

        print("***** TEAM B *****\n")

        print("Shot Distributions: \n")
        print("2PT:", two_point_distr_B)
        print("NC3:", nc_three_distr_B)
        print("C3:", c_three_distr_B, '\n')

        print("Effective Field Goal Percentages: \n")
        print("2PT:", efg_2pt_B)
        print("NC3:", efg_nc_three_B)
        print("C3:", efg_c_three_B)

main()