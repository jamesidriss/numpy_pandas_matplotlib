import pandas as pd

# Lecture du dataframe
food_info = pd.read_csv('food_info.csv')
print(type(food_info))

# Tout afficher
column_names = food_info.columns
print(column_names)

# Ou afficher les 5 premières lignes
print(food_info.head())

# Connaître les types de données
print(food_info.dtypes)

# Connaître les dimensions du dataframe
dimensions = food_info.shape
print(dimensions)

# Accéder au nombre de ligne et colonne
num_rows = dimensions[0]
print(num_rows)

num_cols = dimensions[1]
print(num_cols)

# Sélectionner la 100ème ligne
row_100 = food_info.loc[99]
print(row_100)

# Sélectionner des lignes 3 à 6
food_info.loc[3:6]

# Sélectionner des colonnes
col_name_protein = 'protein_(g)'
protein = food_info[col_name_protein]
print(protein)

cholesterol = food_info['Cholestrl_(mg)']

columns = ['Zinc_(mg)', 'Copper_(mg)']
zinc_copper = food_info[columns]
# ou
zinc_copper = food_info[['Zinc_(mg)', 'Copper_(mg)']]

selenium_thiamin = food_info[['Shrt_Desc', 'Selenium_(mcg)', 'Thiamin_(mg)']]
print(selenium_thiamin)

# Transformer une colonne
div_1000 = food_info['Iron_(mg)'] / 1000
add_100 = food_info['Iron_(mg)'] + 100
sub_100 = food_info['Iron_(mg)'] - 100
mult_2 = food_info['Iron_(mg)'] * 2
sodium_grams = food_info['Sodium_(mg)'] / 1000
sugar_milligrams = food_info['Sugar_Tot_(g)'] * 1000

# Opération entre colonnes
water_energy = food_info['Water_(g)'] * food_info['Energ_Kcal']
print(water_energy[0:5])
print(food_info[['Water_(g)', 'Energ_Kcal']][0:5])

grams_of_protein_per_gram_of_water = food_info['Protein_(g)'] / food_info['Water_(g)']
milligrams_of_calcium_and_iron = food_info['Calcium_(mg)'] + food_info['Iron_(mg)']
print(grams_of_protein_per_gram_of_water)
print(milligrams_of_calcium_and_iron)

# Créer un nouvel indice
food_info['Score'] = 2 * food_info['Normalized_Protein'] - 0.75 * food_info['Normalized_Fat']

# Normaliser des données
max_calories = food_info['Energ_Kcal'].max()
print(max_calories)
# Pour normaliser, on va diviser les valeurs de la colonne 'Energ_Kcal' par la valeur max de cette même colonne
normalized_calories = food_info['Energ_Kcal'] / max_calories
print(normalized_calories)

max_protein = food_info['Protein_(g)'].max()
normalized_protein = food_info['Protein_(g)'] / max_protein
max_fat = food_info['Lipid_Tot_(g)'].max()
normalized_fat = food_info['Lipid_Tot_(g)'] / max_fat
# ou
normalized_protein = food_info['Protein_(g)'] / food_info['Protein_(g)'].max()
normalized_fat = food_info['Lipid_Tot_(g)'] / food_info['Lipid_Tot_(g)'].max()

# Créer une nouvelle colonne
iron_grams = food_info['Iron_(mg)'] / 1000
food_info['Iron_(g)'] = iron_grams

food_info['Normalized_Protein'] = normalized_protein
food_info['Normalized_Fat'] = normalized_fat

# Créer un indice nutritionnel normalisé
score = 2 * normalized_protein - 0.75 * normalized_fat
# On va utiliser les colonnes Normalized_Protein et Normalized_Fat avec cette formule pour créer une nouvelle colonne qu’on nommera Norm_Nutr_Index
food_info['Norm_Nutr_Index'] = 2 * food_info['Normalized_Protein'] - 0.75 * food_info['Normalized_Fat']
food_info['Normalized_Fat'] 
food_info.head()

# Trier par rapport à une colonne
food_info.sort_values('Sodium_(mg)')

# Trier et remplacer le dataframe
# Ordre croissant
food_info.sort_values('Sodium_(mg)', inplace=True)
# Ordre décroissant
food_info.sort_values('Sodium_(mg)', inplace=True, ascending=False)

# ------- Dataframe titanic_survival -------

titanic_survival = pd.read_csv('titanic_survival.csv')

# Traiter les valeurs manquantes
# Trouver les valeurs manquantes
age = titanic_survival['age']
age_is_null = pd.isnull(age)
age_null = age[age_is_null]
age_null_count = len(age_null)
print(age_null_count)
print(age_null)

# Filtrer les valeurs manquantes 
age_is_null = pd.isnull(titanic_survival['age'])
good_ages = titanic_survival['age'][age_is_null == False]
mean_age = sum(good_ages) / len(good_ages)
print(mean_age)

# Calculer la moyenne en ignorant les valeurs manquantes
mean_age = titanic_survival['age'].mean()
print(mean_age)
mean_fare = titanic_survival['fare'].mean()
print(mean_fare)

# Calculer des statistiques de prix
fares_by_class = {}
passenger_classes = [1,2,3]

for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival['pclass'] == this_class]
    pclass_fares = pclass_rows['fare']
    fares_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fares_for_class

print(fares_by_class)

import numpy as np

# Pivot table
passenger_class_fares = titanic_survival.pivot_table(index='pclass', values='fare', aggfunc=np.mean)
print(passenger_class_fares)
passenger_age = titanic_survival.pivot_table(index='pclass', values='age')
print(passenger_age)
passenger_survived = titanic_survival.pivot_table(index='pclass', values='survived')
print(passenger_survived)
port_stats = titanic_survival.pivot_table(index='embarked', values=['fare','survived'], aggfunc=np.sum)
print(port_stats)

# Eliminer les valeurs manquantes
drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=['age', 'sex'])
print(new_titanic_survival.shape) 

# Accéder à des lignes et des colonnes
new_titanic_survival = titanic_survival.sort_values('age', inplace=False, ascending=False)
new_titanic_survival.loc[0] 
new_titanic_survival.iloc[0:5]
first_ten_rows = new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]
new_titanic_survival.iloc[0,0]
new_titanic_survival.iloc[:,0:3]
new_titanic_survival.loc[766, 'pclass']
row_index_1100_age = new_titanic_survival.loc[1100,'age']
row_index_25_survived = new_titanic_survival.loc[25, 'survived']
five_rows_three_cols = new_titanic_survival.iloc[0:5,0:3]

# Réindexer les lignes
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
titanic_reindexed.iloc[0:5,0:3]

# Appliquer une fonction
# Fonction qui retourne le 100ème élément
def row_100(column) :
	# extraire le 100e élément d’une colonne
	item = column.iloc[99]
	return item
    # retourne le 100e element de chaque colonne
row_100_var = titanic_survival.apply(row_100)
# Compter le nombre d'éléments manquants d'un objet series
def null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)

column_null_count = titanic_survival.apply(null_count)
print(column_null_count)

def is_minor(row):
    if row['age'] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)

def which_class(row):
    pclass = row['pclass']
    if pd.isnull(pclass):
        return 'Unknown'
    elif pclass == 1:
        return 'First Class'
    elif pclass == 2:
        return 'Second Class'
    else:
        return 'Third Class'

classes = titanic_survival.apply(which_class, axis=1)

def generate_age_label(row):
    age = row['age']
    if pd.isnull(age):
        return 'Unknown'
    elif age < 18:
        return 'minor'
    else:
        return 'adult'

age_labels = titanic_survival.apply(generate_age_label, axis=1)

# Calculer le pourcentage de survie par groupe d’âge
titanic_survival['age_labels'] = age_labels
age_group_survival = titanic_survival.pivot_table(index='age_labels', values='survived')
print(age_group_survival)
# Ajouter la colonne 'age_labels' au dataframe contenant la variable age_labels qu’on a créée précédemment.
# Créer une table pivot qui calcule la moyenne de chance de survie (colonne 'survived') pour chaque groupe d'âge (colonne 'age_labels') du dataframe.
# Assigner l’objet series résultant de la variable age_group_survival.