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
        
        
def countplot_viz(
    df,
    xcolumn,
    xlabel,
    ylabel,
    title,
    hue=None,
    fontsize_label=16,
    fontsize_title=20,
    fontsize_text=12,
    rotation=45,
    figsize_x=12,
    figsize_y=5,
    palette="viridis",
):
    """
    This function gets a Python Pandas dataframe and visualize a countplot.
    :param data: Dataframe to be analyze
    :param xcolumn: This column designates x axis column.
    :param xlabel: It designates name of x axis column.
    :param ylabel: It designates name of y axis column.
    :param title: This column designates name of graph.
    :param hue: Name of variables in `data` or vector data, optional Inputs for plotting long-form data.
    :param fontsize_label: It designates label size.
    :param fontsize_title: It designates title size.
    :param rotation: It designates rotation of graph.
    :param palette: It designates colors of graph.
    :return: This function doesn't return anything.
    """
    plt.figure(figsize=(figsize_x,figsize_y))
    
    g = sns.countplot(x=xcolumn, data=df, hue=hue, palette=palette, order = df[xcolumn].value_counts().index)
    g.set_title(title, fontsize=19)
    g.set_xlabel(xlabel, fontsize=17)
    g.set_ylabel(ylabel, fontsize=17)
    g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
    plt.tight_layout()
    for p in g.patches:
        height = p.get_height()
        g.text(
            p.get_x() + p.get_width() / 2.0,
            height + 1,
            "{:1}".format(height),
            ha="center",
            fontsize=fontsize_text,
        )    
    if hue != None:
        g.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0)  

def tv_spot_identifier_time_series_chart(
    df, resample_method, spot_list
):
    """
    This function gets a Python Pandas dataframe and visualize a countplot.
    :param df: Dataframe to be visualise
    :param resample_method: Timeseries resampling period
    :return: This function doesn't return anything.
    """

    # sessions_final_df_reporting_df.set_index("date_hour_minute", inplace=True)
    ax = df.resample(resample_method).apply(sum).plot(figsize=(20, 6))
    trans = ax.get_xaxis_transform()
    ax.axvline(spot_list[0], color="red", linestyle="dashed")
    ax.axvline(spot_list[1], color="red", linestyle="dashed")
    ax.axvline(spot_list[2], color="red", linestyle="dashed")
    ax.axvline(spot_list[3], color="red", linestyle="dashed")
    ax.axvline(spot_list[4], color="red", linestyle="dashed")

    plt.text(spot_list[0], 0.8, "First spot air", transform=trans)
    plt.text(spot_list[1], 0.7, "Second spot air", transform=trans)
    plt.text(spot_list[2], 0.8, "Third spot air", transform=trans)
    plt.text(spot_list[3], 0.7, "Fourth spot air", transform=trans)
    plt.text(spot_list[4], 0.8, "Fifth spot air", transform=trans)

    plt.show()        
