import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from sklearn import metrics

data = pd.read_csv('X24.csv')
data[(data.isnull())] = 0

posi = data.loc[data['AKI'] == 1]
nega = data.loc[data['AKI'] == 0]

##  48h  910
##  24h  1025
k=1
i=140

m = int(i*k)
p = posi.sample(n=i, axis=0)
n = nega.sample(n=m, axis=0)
frames = [p, n]
result = pd.concat(frames)
re = shuffle(result)
re.reset_index(drop=True, inplace=True)
target = 'AKI'


def modelfit(alg, dtrain, dtest, predictors, useTrainCV=True, cv_folds=10, early_stopping_rounds=50):

    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(
            dtrain[predictors].values, label=dtrain[target].values)
        xgtest = xgb.DMatrix(dtest[predictors].values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
                          early_stopping_rounds=early_stopping_rounds)
        alg.set_params(n_estimators=cvresult.shape[0])

    #建模
    alg.fit(dtrain[predictors], dtrain['AKI'], eval_metric='auc')

    #对训练集预测
    dtrain_predictions = alg.predict(dtrain[predictors])
    dtrain_predprob = alg.predict_proba(dtrain[predictors])[:, 1]

    #输出模型的一些结果
    print("Stopped at iteration: {0}".format(cvresult.shape[0]))
    print("\n关于现在这个模型")
    print("准确率 : %.4g" % metrics.accuracy_score(
        dtrain['AKI'].values, dtrain_predictions))
    print("AUC 得分 (训练集): %f" % metrics.roc_auc_score(
        dtrain['AKI'], dtrain_predprob))


#获得最佳决策树数目
predictors = [x for x in re.columns if x not in [target]]
xgb1 = XGBClassifier(
    learning_rate=0.1,
    n_estimators=1000,
    max_depth=5,
    min_child_weight=1,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    objective='binary:logistic',
    nthread=4,
    scale_pos_weight=1,
    seed=27)
modelfit(xgb1, re, data, predictors)
                


