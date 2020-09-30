import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
data = pd.read_excel('treat-pure.xlsx')
out = pd.ExcelWriter('numlize.xlsx')
data.drop(['day', 'pid'], axis=1, inplace=True)
data.reset_index(drop=True, inplace=True)
data[(data.isnull())] = 0
data[(data != 0)] = 1
data.to_excel(out, 'Sheet1')
out.save()
