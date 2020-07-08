import matplotlib.pyplot as plt
import texthero as hero
import pandas as pd
import pickle

csv_df = pd.read_csv('mpesa.csv')

csv_df['pca'] = (
            csv_df['Details']
            .pipe(hero.clean)
            .pipe(hero.tfidf)
            .pipe(hero.pca)
   )

hero.scatterplot(csv_df, col='pca', color='Details', title="M-pesa Transactions")

NUM_TOP_WORDS = 5
csv_df.groupby('Details')['Paid In'].apply(lambda x: hero.top_words(x)[:NUM_TOP_WORDS])