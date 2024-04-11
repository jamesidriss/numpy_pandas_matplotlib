import pandas as pd

reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

norm_reviews = reviews[cols]

# Distribution de fréquence
imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
imdb_distribution = imdb_distribution.sort_index()

print(imdb_distribution)

# Créer un sous-graphique et assigner les objets Figure à la variable fig et Axes à la variable ax
# Générer un histogramme des valeurs de la colonne 'Fandango_Ratingvalue' en utilisant un range de 0 à 5
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(0,5))
plt.show()

# Comparaison d'historigrammes

# Tracer un graphique avec 4 sous-graphiques:
# - Sous-graphique associé à la variable ax1:
# Générer un histogramme des valeurs de la colonne 'Fandango_Ratingvalue' en utilisant 20 classes (bins) et un intervalle de 0 à 5
# - Sous-graphique associé à la variable ax2:
# Générer un histogramme des valeurs de la colonne 'RT_user_norm' en utilisant 20 classes (bins) et un intervalle de 0 à 5
# - Sous-graphique associé à la variable ax3:
# Générer un histogramme des valeurs de la colonne 'Metacritic_user_nom' en utilisant 20 classes (bins) et un intervalle de 0 à 5
# - Sous-graphique associé à la variable ax4:
# Générer un histogramme des valeurs de la colonne 'IMDB_norm' en utilisant 20 classes (bins) et un intervalle de 0 à 5
# - Pour tous les graphiques définir l'intervalle sur l'axe y de 0 à 50 en utilisant Axes.set_ylim() et définir le titre
fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews['Fandango_Ratingvalue'], bins=20, range=(0,5))
ax1.set_title('Distribution des notes de fandango')
ax1.set_ylim(0,50)

ax2.hist(norm_reviews['RT_user_norm'], bins=20, range=(0,5))
ax2.set_title('Distribution des notes de Rotten Tomatoes')
ax2.set_ylim(0,50)

ax3.hist(norm_reviews['Metacritic_user_nom'], bins=20, range=(0,5))
ax3.set_title('Distribution des notes de Metacritic')
ax3.set_ylim(0,50)

ax4.hist(norm_reviews['IMDB_norm'], bins=20, range=(0,5))
ax4.set_title('Distribution des notes de IMDB')
ax4.set_ylim(0,50)

plt.show()