import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def errorPlot(df, variables, star_ids):
    if not (isinstance(variables, list)):
        print("Variable names must be a list of strings")
    elif not (isinstance(star_ids, list)):
        print("Star ID must be a list of strings")
    elif not isinstance(df, pd.core.frame.DataFrame):
        print("Argument must be a pandas dataframe")
    else:
        with_uncer = []
        for variable in variables:
            if not variable in df.columns:
                print(variable + "is not a valid variable name")
            if "e_" + variable in df.columns:
                with_uncer.append(variable)
            else: 
                print("The variable " + variable + "does not have an associated uncertainty")
        id_var_err = {}
        #indeces = [df[df["star_id"] == starid].index[0] for starid in star_ids]
        for star_id in star_ids:
            index = df[df["star_id"] == star_id].index[0]
            id_var_err[star_id] = [[df[x][index] for x in with_uncer], [df["e_" + x][index] for x in with_uncer]]
        plt.figure()
        x_marks = np.arange(len(with_uncer))
        for star_id in star_ids:
            plt.errorbar(x_marks, id_var_err[star_id][0], yerr=id_var_err[star_id][1], label=star_id, marker="o")
        plt.xticks(x_marks, with_uncer)
        plt.show()
        return id_var_err


test1000 = pd.read_csv("TOP1000.csv")

df = pd.DataFrame(test1000)
variables = ["al_fe", "ba_fe", "eu_fe"]
stars= ["13321909-7822135", "13322043-3651561"]
#index1 = df[df["star_id"] == stars[0]].index.values
print(errorPlot(df,variables, stars))