import pandas as pd
import numpy as np
from pandas import Series, DataFrame
statu = pd.read_csv('X-fill.csv')
treat = pd.read_csv('output.csv')
pid = pd.read_csv('pid.csv')
path='X.csv'

statu1=statu.iloc[::2].copy()
statu1.reset_index(drop=True, inplace=True)

statu2 = statu.iloc[1::2].copy()
statu2 = statu2.rename(columns=lambda x: x.replace('statu', 'st'))
statu2.reset_index(drop=True, inplace=True)

result1 = pd.merge(statu1, statu2, how='inner', on='pid')

result = pd.merge(result1, treat, how='inner', on='pid')

pid.drop(['day'], axis=1, inplace=True)
total = pd.merge(pid, result, how='inner', on='pid')
total.to_csv(path)


