import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import astropy



def read_input(filename):
    '''
    This function takes in a csv file containing the data desired to analysed and
    returns a pandas dataframe containing the data. 

    Args: 
        filename (str): The path to the file
    
    Output: 
        data (DataFrame): The data in the form of a pandas Dataframe
    '''
    data=pd.read_csv(filename)
    return data

