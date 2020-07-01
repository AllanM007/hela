import pandas as pd
import matplotlib.pyplot as plt

csv_df = pd.read_csv('mpesa.csv')

#csv_df.dropna(inplace = True) 

sub ='Pay Bill'

start = 0

df = csv_df['Details'].str.find(sub, start)

print(df)