import pandas as pd

#load the dataset
df = pd.read_csv("results.csv")
#store in a csv file 
df.groupby(['Province']).max().to_csv("max.csv")
df.groupby(['Province']).min().to_csv("min.csv")
df.groupby(['Model']).mean().to_csv("mean.csv")
