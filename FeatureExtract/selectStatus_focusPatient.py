import pandas as pd
from pandas import Series, DataFrame
data = pd.read_excel('statustest.xlsx')
out = pd.ExcelWriter('status-parttest.xlsx')
pid = pd.read_excel('pid-test.xlsx')
put = pd.read_excel('status-parttest.xlsx')

for index, row in pid.iterrows():
    if(row['AKI'] == 1):
        temp = data[(data['pid'] == row['pid']) & (data['day'] < row['day']) & (data['day'] >= 0)].copy()
        put = pd.concat([put, temp], axis=0, sort=False)
    else:
        temp = data[(data['pid'] == row['pid']) & (data['day'] >= 0)].copy()
        put = pd.concat([put, temp], axis=0, sort=False)
put.to_excel(out, 'Sheet1')
out.save()
