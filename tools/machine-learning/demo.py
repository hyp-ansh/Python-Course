import pandas as pd

csv = pd.read_csv('tools\misc\machine-learning\sample.csv')
s_csv = csv[['name', 'number']]
print(s_csv)