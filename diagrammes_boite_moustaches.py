import pandas as pd

reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

norm_reviews = reviews[cols]

# Plusieurs diagrammes à boîte / boite à moustaches
import matplotlib.pyplot as plt
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB