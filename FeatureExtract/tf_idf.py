import math
import pandas as pd
start = pd.read_csv('input.csv')
pid = pd.read_csv('pid-test.csv')
form = pd.read_csv('X-partfor.csv')
form[(form.isnull())] = 0
path = 'output.csv'
length = len(start)
start.loc['sum'] = start.apply(lambda x: x.sum())
for index0, row0 in pid.iterrows():
    temp = start[(start['pid'] == row0['pid'])].copy()
    temp.drop(['pid'], axis=1, inplace=True)
    for index1, row1 in temp.iterrows():
        for ix, col in temp.iteritems():
            x = math.log((length+1)/(start.loc['sum', ix]+1)+1)
            xx = temp.loc[index1, ix]*x
            form.loc[index1, ix] = xx
form.to_csv(path)
