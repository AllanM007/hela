import matplotlib.pyplot as plt
import pandas as pd
import pickle
import nltk

csv_df = pd.read_csv('mpesa.csv')

#starting point for keyword search
a = 0

#function to check loan keyword in csv column
def loans():
    df = deets = csv_df['Details'].str.contains("Loan")

    for t in df:
        if t == True:
            print("You took {} loans".format(sum(df)))
        else:
            print("Uko Sawa")
    else:
        pass

nltk.download('punkt')

#transform column to list
deets = csv_df['Details'].to_list()

#apply tokenization function to column values
tokens = csv_df.apply(lambda row: nltk.word_tokenize(row['Details']), axis=1)

loans()