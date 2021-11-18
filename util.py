import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")

def file_read():
    """
    This function allows us to read all the Excel and Csv files into data frames.
    After the initial reading, we delete rows which all columns are null.
    :return: Dataframes
    """
    sessions_final_df = pd.read_csv("case_may_2020_sessions_final.csv")
    tv_data_df = pd.ExcelFile("case_may_2020_TV_data.xlsx")
    audience_df = tv_data_df.parse("Audience", usecols=["tv_show", "reach"])
    tv_planning_df = tv_data_df.parse("TV Planning")
    tv_spots_df = tv_data_df.parse("TV spots")
    tv_visits_match_df = tv_data_df.parse("TV - visits match")

    sessions_final_df.dropna(axis=0, how="all", inplace=True)
    audience_df.dropna(axis=0, how="all", inplace=True)
    tv_planning_df.dropna(axis=0, how="all", inplace=True)
    tv_spots_df.dropna(axis=0, how="all", inplace=True)
    tv_visits_match_df.dropna(axis=0, how="all", inplace=True)

    return sessions_final_df, audience_df, tv_planning_df, tv_spots_df, tv_visits_match_df

def sessions_final_df_cleaning(sessions_final_df,channel_list):
    """
    This function gathers a list from the user to parse the data frame to include the given channels.
    :param channel_list: Channel list object to be parsed
    :return: Dataframe
    """
    sessions_final_df_correct_channels = sessions_final_df[
        sessions_final_df["channel"].isin(channel_list)
    ].copy()

    del sessions_final_df_correct_channels["Unnamed: 0"]

    return sessions_final_df_correct_channels


def df_first_look(df):
    """
    This function gets a Python Pandas dataframe and visualize basic information about the dataframe.
    :param df: Dataframe to be analyze
    :return: This function doesn't return anything.
    """
    try:
        print("First 5 rows of dataframe:\n--------------------------\n", df.head())
        print("")
        print("Last 5 rows of dataframe:\n--------------------------\n", df.tail())
        print("")
        print(
            "Row count of dataframe:\n-----------------------\n",
            df.shape[0],
            "\nColumn count of dataframe:\n--------------------------\n",
            df.shape[1],
        )
        print("")
        print(
            "List of columns in the dataframe:\n---------------------------------\n",
            df.columns.values,
        )
        print("")
        print(
            "Looking NaN values and datatypes of columns in the dataframe:\n--------------------------------------------\n"
        )
        print(df.info())
        print("")

    except Exception as e:
        print("Error at df_first_look function: ", str(e))