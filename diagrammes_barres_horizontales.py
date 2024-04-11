import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

# Importation des données
reviews = pd.read_csv("fandango_scores.csv")

# Sélection des colonnes pertinentes
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]
print(norm_reviews[:3])

# Définition des données pour le graphique
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 1
tick_positions = range(1, 6)

# Création du graphique à barres horizontales
fig, ax = plt.subplots()
ax.barh(bar_positions, bar_widths, 0.5)

# Définition des étiquettes de l'axe y et des titres des axes
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
ax.set_ylabel('Sou