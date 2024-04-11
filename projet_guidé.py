import pandas as pd

data = pd.read_csv('thanksgiving.csv', encoding='Latin-1')
print(data.head())

# Filtrer les données
print(data['Do you celebrate Thanksgiving?'].value_counts())
# On supprime les réponses "non" inutiles
data = data[data['Do you celebrate Thanksgiving?'] == 'Yes']

# Exploration
print(data['What is typically the main dish at your Thanksgiving dinner?'].value_counts())

tofurkey = data[data['What is typically the main dish at your Thanksgiving dinner?'] == 'Tofurkey']
print(tofurkey)

apple_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'])
pumpkin_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - pumpkin'])
pecan_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'])
pies = apple_isnull & pumpkin_isnull & pecan_isnull
print(pies.value_counts())

# Convertir en valeur numérique
print(data['Age'].value_counts())

def extract_age(age_str):
    if pd.isnull(age_str):
        return None
    age_str = age_str.split(' ')[0]
    age_str = age_str.replace('+', '')
    return int(age_str)

data['int_age'] = data['Age'].apply(extract_age)
print(data['int_age'].describe())

print(data['How much total combined money did all members of your HOUSEHOLD earn last year?'].value_counts())

def extract_income(income_str):
    if pd.isnull(income_str):
        return None
    income_str = income_str.split(' ')[0]
    if income_str == 'Prefer':
        return None
    income_str = income_str.replace(',', '')
    income_str = income_str.replace('$', '')
    return int(income_str)

data['int_income'] = data['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(extract_income)
print(data['int_income'].describe())

less_150000 = data[data['int_income'] < 150000]
print(less_150000['How far will you travel for Thanksgiving?'].value_counts())

more_150000 = data[data['int_income'] > 150000]
print(more_150000['How far will you travel for Thanksgiving?'].value_counts())

# Lien entre passer Thanksgiving entre amis avec l’âge et le revenu
print(data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns="Have you ever attended a 'Friendsgiving?'",values='int_age'))

print(data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns="Have you ever attended a 'Friendsgiving?'",values='int_income'))