import pandas as pd
import numpy as np
statu = pd.read_csv('status-parttest.csv')
pid = pd.read_csv('pid-test.csv')
pid[(pid.isnull())] = 0
put = pd.DataFrame()
path = "X-filltest.csv"
statu.drop(['day'], axis=1, inplace=True)
statu.loc['mean'] = statu.apply(lambda x: x.mean())
for index0, row0 in pid.iterrows():
    temp = statu[(statu['pid'] == row0['pid'])]
    i=0
    for index1, row1 in temp.iterrows():
        i=i+1
        if(i==1):
            for ix, col in temp.iteritems():
                if(np.isnan(temp.loc[index1, ix])):
                    m = index1
                    while(m+1 <= len(temp)-1):
                        if(np.isnan(temp.loc[m+1, ix])):
                            m = m+1
                        else:
                            #statu.loc[index1, ix] = temp.loc[m+1, ix]
                            temp.loc[index1, ix] = temp.loc[m+1, ix]
                            break
                if(np.isnan(temp.loc[index1, ix])):
                    #statu.loc[index1, ix] = statu.loc['mean', ix]
                    temp.loc[index1, ix] = statu.loc['mean', ix]
            y=row1
            put = pd.concat([put, y], axis=1,sort=False)
        if((i == len(temp))&(row0['AKI']==0)):
            for ix, col in temp.iteritems():
                if(np.isnan(temp.loc[index1, ix])):
                    x=len(temp)
                    m = index1
                    while(x-1>0):
                        if(np.isnan(temp.loc[m-1, ix])):
                            m = m-1
                            x=x-1
                        else:
                            #statu.loc[index1, ix] = temp.loc[m-1, ix]
                            temp.loc[index1, ix] = temp.loc[m-1, ix]
                            break
                if(np.isnan(temp.loc[index1, ix])):
                    #statu.loc[index1, ix] = statu.loc['mean', ix]
                    temp.loc[index1, ix] = statu.loc['mean', ix]
            y=row1
            put = pd.concat([put, y], axis=1, sort=False)
        if((i == (len(temp)-1) )&( row0['AKI'] == 1)):
            for ix, col in temp.iteritems():
                if(np.isnan(temp.loc[index1, ix])):
                    x = len(temp)-1
                    m = index1
                    while(x-1 > 0):
                        if(np.isnan(temp.loc[m-1, ix])):
                            m = m-1
                            x = x-1
                        else:
                            #statu.loc[index1, ix] = temp.loc[m-1, ix]
                            temp.loc[index1, ix] = temp.loc[m-1, ix]
                            break
                if(np.isnan(temp.loc[index1, ix])):
                    #statu.loc[index1, ix] = statu.loc['mean', ix]
                    temp.loc[index1, ix] = statu.loc['mean', ix]
            y = row1
            put = pd.concat([put, y], axis=1,sort=False)
put=put.T
put.to_csv(path, index=False,header=True)
