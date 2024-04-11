import numpy as np
import pandas as pd

# Importer le fichier et afficher les 5 premières lignes
all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')
print(all_ages.head())
print(recent_grads.head())

# Nombre d’étudiants par catégorie de Major
print(all_ages['Major_category'].unique())

# Fonction avec la colonne Total pour calculer le nombre d’étudiants pour chaque catégorie de Major 
def calculate_major_cat_totals(df):
    cats = df['Major_category'].unique()
    counts_dictionary = dict()

    for c in cats:
        major_df = df[df['Major_category'] == c]
        total = major_df['Total'].sum()
        counts_dictionary[c] = total

    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
print(aa_cat_counts)

rg_cat_counts = calculate_major_cat_totals(recent_grads)
print(rg_cat_counts)

# Table pivot
aa_cat_counts_ = all_ages.pivot_table(index='Major_category', values='Total', aggfunc=np.sum)
print(aa_cat_counts_)

# Taux d'emploi à faible salaire
low_wage_jobs_sum = recent_grads['Low_wage_jobs'].sum()
recent_grads_sum = recent_grads['Total'].sum()
low_wage_proportion = low_wage_jobs_sum / recent_grads_sum
print(low_wage_proportion)

# Comparer des datasets
majors = recent_grads['Major'].unique()

rg_lower_count = 0

for m in majors:
    recent_grads_row = recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]

    rg_unemp_rate = recent_grads_row['Unemployment_rate'].values
    aa_unemp_rate = all_ages_row['Unemployment_rate'].values

    if rg_unemp_rate < aa_unemp_rate:
        rg_lower_count += 1

print(rg_lower_count)
# Utiliser une boucle for pour parcourir toutes les majors
# Pour chaque Major et chaque DataFrame, filtrer seulement les lignes du DataFrame correspondant à cette major
# Comparer les valeurs pour la colonne ‘Unemployment_rate’ pour voir lequel des 2 dataframes possèdent la valeur la plus basse
# Incrémenter à la variable rg_lower_count si la valeur pour Unemployment_rate est plus petite dans la dataframe recent_grads que dans le dataframe all-ages
# Afficher le résultat rg_lower_count