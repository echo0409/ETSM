import pandas as pd
pid = pd.read_csv('pid-test.csv')
path = 'numlizetest.csv'
path1 = 'full.csv'
data = pd.read_csv('treatmenttest.csv')
put = pd.DataFrame()
for index, row in pid.iterrows():
    if(row['AKI'] == 1):
        temp = data[(data['pid'] == row['pid']) & (data['day'] < row['day']) & (data['day'] >= 0)].copy()
        put = pd.concat([put, temp], axis=0)
    else:
        temp = data[(data['pid'] == row['pid']) & (data['day'] >= 0)].copy()
        put = pd.concat([put, temp], axis=0)

put.drop(['day'], axis=1, inplace=True)
put.reset_index(drop=True, inplace=True)
put.to_csv(path1)
put.drop(['pid'], axis=1, inplace=True)
put[(put.isnull())] = 0
put[(put != 0)] = 1
put.to_csv(path)
