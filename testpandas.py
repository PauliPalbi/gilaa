import pandas as pd
teststars = pd.read_csv("testdata.csv")

df = pd.DataFrame(teststars)

print(len(df["flag_eu_fe"]))