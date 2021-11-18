import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")


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