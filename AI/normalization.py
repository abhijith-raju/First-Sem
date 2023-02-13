import pandas as pd

df = pd.read_csv('Affairs.csv')

dummies = pd.get_dummies(df.gender)

merged = pd.concat([df, dummies], axis='columns')


merged1 = merged.drop(['gender'], axis='columns')

print(merged1)

