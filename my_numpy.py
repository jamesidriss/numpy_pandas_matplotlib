import numpy as np

# Création tableau :
vector = np.array([3, 4, 17, 65])
# création matrice :
matrix = np.array([[2, 5, 15], [20, 50, 30], [34, 99, 45]])

# Dimensions :
print("Dimensions du vecteur:", vector.shape)
print("Dimensions de la matrice:", matrix.shape)

# Type de données
print("Type de données du vecteur:", vector.dtype)
print("Type de données de la matrice:", matrix.dtype)

# Lecture du dataset world_alcohol
world_alcohol = np.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
print(type(world_alcohol))
print(world_alcohol)

# Extraire une valeur
ivoire_1985 = world_alcohol[2,4]
print(ivoire_1985)

second_country = world_alcohol[1,2]
print(second_country)

# Extraire un tableau de valeur
first_two_columns = world_alcohol[:,0:2]
first_ten_years = world_alcohol[0:10,0]
first_ten_rows = world_alcohol[0:10,:]
first_twenty_regions = world_alcohol[0:20,1:3]

# Comparaison
countries_canada = (world_alcohol[:,2] == 'Canada')
years_1984 = (world_alcohol[:, 0] == '1984')

# Selectionner des éléments
country_is_algeria = world_alcohol[:,2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria]
print(country_algeria)

years_1984 = world_alcohol[world_alcohol[:,0] == '1984']
print(years_1984)

# Comparaisons avec plusieurs conditions
is_algeria_and_1986 = (world_alcohol[:,2] == 'Algeria') & (world_alcohol[:,0] == '1986')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]
print(rows_with_algeria_and_1986)

# Remplacer des valeurs
world_alcohol_2 = world_alcohol.copy()
world_alcohol_2[:,0][world_alcohol_2[:,0] == '1986'] = '2018'
world_alcohol_2[:,3][world_alcohol_2[:,3] == 'Wine'] = 'Beer'

# Remplacer les chaines de caractères vides
is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'

# Convertir des types de données
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)
print(alcohol_consumption)

# Calcul mathématiques
total_alcohol = alcohol_consumption.sum()
print(total_alcohol)

average_alcohol = alcohol_consumption.mean()
print(average_alcohol)