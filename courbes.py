import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

# Afficher un graphique vide
plt.plot()
plt.show()

# Ajouter des données au graphique
first_year = unrate.head(12)
plt.plot(first_year['DATE'], first_year['UNRATE'])
plt.show()

# Créer des rotations sur les données de l'axe x
plt.plot(first_year['DATE'], first_year['UNRATE'])
plt.xticks(rotation=90)
plt.show()

# Ajouter des intitulés
plt.plot(first_year['DATE'], first_year['UNRATE'])
plt.xticks(rotation=90)
plt.xlabel('Mois')
plt.ylabel('Taux de chômage (%)')
plt.title('Évolution du taux de chômage en 1948 aux USA')

# Ajouter un objet figure avec plusieurs sous-graphiques
fig, axs = plt.subplots(2, 1)

# Sous-graphiques
fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

# Ajouter des données et ajuster les dimensions
fig = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['UNRATE'])
ax1.set_title('Taux de chômage en 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['UNRATE'])
ax2.set_title('Taux de chômage en 1949')
plt.show()

# Comparaison de graphiques
fig = plt.figure(figsize=(12,12))

for i in range(5):
       ax = fig.add_subplot(5,1,i+1)
       start_index = i*12
       end_index = (i+1)*12
       subset = unrate[start_index:end_index]
       ax.plot(subset['DATE'], subset['UNRATE'])
plt.show()

# Superposition des courbes
unrate['MONTH'] = unrate['DATE'].dt.month

# Générer plusieurs courbes
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['UNRATE'])
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['UNRATE'])

# Définir les dimensions de la zone d'affichage
fig = plt.figure(figsize=(6,6))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['UNRATE'])
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['UNRATE'])
plt.show()

# Changer les couleurs
fig = plt.figure(figsize=(6,6))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['UNRATE'])
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['UNRATE'], c='red')
plt.show()

# Afficher plus de courbes
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']

for i in range(5):
       start_index = i*12
       end_index = (i+1)*12
       subset = unrate[start_index:end_index]

       plt.plot(subset['MONTH'], subset['UNRATE'], c=colors[i])

plt.show()

# Ajouter une légende
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['UNRATE'], c='red', label='1948')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['UNRATE'], c='blue', label='1949')

# Dimensions de la zone d'affichage
fig = plt.figure(figsize=(6,6))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['UNRATE'])
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['UNRATE'])
plt.legend(loc='upper left')
plt.show()

# Afficher une légende pour chaque sous-graphique
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']

for i in range(5):
       start_index = i*12
       end_index = (i+1)*12
       subset = unrate[start_index:end_index]
       label = str(1948 + i)
       plt.plot(subset['MONTH'], subset['UNRATE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.show()

# Courbe finale :
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']

for i in range(5):
       start_index = i*12
       end_index = (i+1)*12
       subset = unrate[start_index:end_index]
       label = str(1948 + i)
       plt.plot(subset['MONTH'], subset['UNRATE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title('Évolution du taux de chômage de 1948 à 1952')
plt.xlabel('Mois (de 1 à 12)')
plt.ylabel('Taux de chômage (en %)')
plt.show()