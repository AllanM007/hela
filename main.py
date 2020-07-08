from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import pandas as pd
import pickle

csv_df = pd.read_csv('mpesa.csv')

csv_df.dropna(inplace = True)

sub ='Loan'

dotcom = csv_df["Balance"].values.tolist()

a = 0

def loans():
    df = csv_df['Details'].str.find(sub)

    for t in df:
        if t >= a:
            print("You took a loan")
        else:
            print("Uko Sawa")
    else:
        pass

#print(dotcom)
loans