import pandas as pd
from pandas import Series, DataFrame
data = pd.read_excel('treat-pure.xlsx')
out = pd.ExcelWriter('dictionary.xlsx')
data.drop(['day', 'pid'], axis=1, inplace=True)
data.reset_index(drop=True, inplace=True)
data[(data.isnull())] = 0
data[(data != 0)] = 1
data = data.drop_duplicates()
data.reset_index(drop=True, inplace=True)
data.to_excel(out, 'Sheet1')
out.save()
