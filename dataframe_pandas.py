import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
print(fandango.head(2))

print(fandango.index)

print(fandango.iloc[140:])

first_last = fandango.iloc[[0, -1]]
print(first_last)

fandango_films = fandango.set_index('FILM', drop=False)

print(fandango_films.loc['Mr. Holmes (2015)':'Two Days, One Night (2014)'])
# Tous les films depuis Mr. Holmes jusqu’à Two Days, One Night

# Chercher un film
print(fandango_films.loc['Kumiko, The Treasure Hunter (2015)'])

# Sélectionner des lignes multiples
movies = ['Top Five (2014)', 'Black Sea (2015)', 'Taken 3 (2015)']
some_movies = fandango_films.loc[movies]
print(some_movies)

import numpy as np
types = fandango_films.dtypes
print(types)

float_columns = types[types == 'float64'].index
print(float_columns)

float_df = fandango_films[float_columns]
print(float_df)

types = fandango_films.dtypes
float_columns = types[types == 'float64'].index
float_df = fandango_films[float_columns]
exo_df = float_df.apply(lambda x: x / 2)
print(exo_df.head())

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
print(rt_mt_user)
print(rt_mt_user.apply(np.std, axis=1))