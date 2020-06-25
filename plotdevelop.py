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
        self.data=data
        self.df = pd.DataFrame(self.data)

    def plot_abundance(self,starname,elements,save=False,savename=False):
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
        for i in starname:
            print("Starnames: {}".format(i))
        for i in elements:
            print("Elements: {}".format(i))

        #create a list of the column labels corresponding to the desired labels
        
        labels=[]
        
        for i in elements:
            print(i)
            label=i.lower()+'_fe'

            assert (label in star.data.columns), "{} not found in data file".format(label)
            labels.append(label)
        

        #get abundance values for the star:
        
        self.data.set_index('star_id',inplace=True)
        star_data = [[], [], []]
        abundances=[{}, {}, {}]

        for i in range(len(starname)):
           star_data[i]=self.data.loc[starname[i]]
           for label in labels:
                abundances[i][label]=star_data[i][label]
        
        # sort alphabetically
        alph_keys=sorted(abundances[0].keys(), key=lambda x:x.lower())
        values = [[], [], []]
        for i in range(len(starname)):
            values[i]=[abundances[i][k] for k in alph_keys]
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        colors = ["red", "green", "blue"]
        for i in range(len(starname)):
            ax.bar(alph_keys, values[i], width=0.2, color=colors[i])
        
        ax.set_xlabel("[Element/Fe]")
        ax.set_ylabel("Abundance")
        #ax.title("Chemical Abundances of 2MASS {}".format(starname))
        fig.savefig('{}.png'.format(savename))
        fig.show()

        return abundances
        
if __name__ == "__main__":
    data=pd.read_csv("testdata.csv")
    star=plot(data)
    starname=star.data['star_id'][0:3]

    print(star.plot_abundance(starname,['o','ca','ba','c','ti','mg'],save=True,savename='test_abundances'))