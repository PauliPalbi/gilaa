import numpy as np 
import matplotlib.pyplot as plt
import astropy
import pandas as pd

class plot(object):
    '''
    A class to do all the plotting from.
    Args:
        data (pandas DataFrame): a dataframe containing the data desired to be
                                 plotted.
    
    '''
    def __init__(self, data):
        self.data=data.set_index('star_id')

    def plot_abundance(starname,elements=None,save=False,savename=False):
        '''
        Plots the elemental abundances of a given star as a bar plot.

        Args: 
            starname (str) : The star-id of the star for which the user wishes
                             to plot abundances
            elements (list): A list signifying which elemental abundances
                             the user wishes to plot. Must be in the format
                             of the galah datafiles
            save (Boolean) : Indicates whether the created plot should be 
                             saved or not. The default setting is False.
            savename (str) : If save is set to True, a savename must be 
                             provided.
        Returns:
            matplotlib.pyplot.Figure: the orbit plot if input is valid, ``None`` otherwise 
    
        '''
        
        return None
        #deets=data[starname]
        
if __name__ == "__main__":
    star=plot(pd.read_csv('./data/ngc632.csv'))
    print(star.data[0])
