import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

# Indexage avec des entiers
series_film = fandango['FILM']
print(series_film.iloc[0:5])
series_rt = fandango['RottenTomatoes']
print(series_rt.iloc[0:5])

# Personnaliser l'indexage
# Extraire les notes RottenTomatoes pour de nombreux films en même temps avec une seule commande
film_names = series_film.values
rt_scores = series_rt.values
series_custom = pd.Series(rt_scores, index=film_names)
print(series_custom[['Minions (2015)', 'Leviathan (2014)']])
print(series_custom.iloc[5:11])

# Réindexer un objet Series
original_index = series_custom.index
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index)

# Trier un objet series
sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2.iloc[0:10])
print(sc3.iloc[0:10])

# Transformation de colonne
import numpy as np
print(np.add(series_custom, series_custom))
print(np.sin(series_custom))
print(np.max(series_custom))
series_normalized = series_custom / 20
print(series_normalized)

# Comparer et filtrer
series_greater_than_50 = series_custom[series_custom > 50]
criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
print(series_greater_than_50)
print(both_criteria)

# Alignement des données
rt_critics = pd.Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = pd.Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics + rt_users) / 2
print(rt_mean)