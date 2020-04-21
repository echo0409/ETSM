#max_depth 和 min_weight 参数调优
#n_estimators取上一步的最优值
param_test1 = {
    'max_depth': range(3, 10, 2),
    'min_child_weight': range(1, 6, 2)
}
gsearch1 = GridSearchCV(estimator=XGBClassifier(learning_rate=0.1, n_estimators=140, max_depth=5,
                                                min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8,
                                                objective='binary:logistic', nthread=4, scale_pos_weight=1, seed=27),
                        param_grid=param_test1, scoring='roc_auc', n_jobs=4, iid=False, cv=5)
gsearch1.fit(train[predictors], train[target])
print(gsearch1.cv_results_, gsearch1.best_params_, gsearch1.best_score_)
#max_depth 和 min_weight 参数调优进一步调优
#n_estimators取上一步的最优值
param_test2 = {
    'max_depth': [4, 5, 6],
    'min_child_weight': [4, 5, 6]
}
gsearch2 = GridSearchCV(estimator=XGBClassifier(learning_rate=0.1, n_estimators=140, max_depth=5,
                                                min_child_weight=2, gamma=0, subsample=0.8, colsample_bytree=0.8,
                                                objective='binary:logistic', nthread=4, scale_pos_weight=1, seed=27),
                        param_grid=param_test2, scoring='roc_auc', n_jobs=4, iid=False, cv=5)
gsearch2.fit(train[predictors], train[target])
print(gsearch2.cv_results_, gsearch2.best_params_, gsearch2.best_score_)

#gamma参数调优
#节点分裂所需的最小损失函数下降值，这个参数的值越大，算法越保守
#n_estimators，max_depth 和 min_weight 取上一步的最优值
param_test3 = {
    'gamma': [i/10.0 for i in range(0, 5)]
}
gsearch3 = GridSearchCV(estimator=XGBClassifier(learning_rate=0.1, n_estimators=140, max_depth=4, min_child_weight=6, gamma=0, subsample=0.8, colsample_bytree=0.8,
                                                objective='binary:logistic', nthread=4, scale_pos_weight=1, seed=27), param_grid=param_test3, scoring='roc_auc', n_jobs=4, iid=False, cv=5)

gsearch3.fit(train[predictors], train[target])
print(gsearch3.cv_results_, gsearch3.best_params_, gsearch3.best_score_)

#调整subsample 和 colsample_bytree 参数
#subsample参参数控制对于每棵树，随机采样的比例
#colsample_bytree 参数控制每棵随机采样的列数的占比(每一列是一个特征)
#gamma，n_estimators，max_depth 和 min_weight 取上一步的最优值
param_test4 = {
 'subsample':[i/10.0 for i in range(6,10)],
 'colsample_bytree':[i/10.0 for i in range(6,10)]
}

gsearch4 = GridSearchCV(estimator = XGBClassifier( learning_rate =0.1, n_estimators=177, max_depth=3, min_child_weight=4, gamma=0.1, subsample=0.8, colsample_bytree=0.8, objective= 'binary:logistic', nthread=4, scale_pos_weight=1,seed=27), param_grid = param_test4, scoring='roc_auc',n_jobs=4,iid=False, cv=5)
gsearch4.fit(train[predictors],train[target])
print(gsearch4.cv_results_, gsearch4.best_params_, gsearch4.best_score_)

#进一步调整subsample 和 colsample_bytree 参数
#gamma，n_estimators，max_depth 和 min_weight 取上一步的最优值
param_test5 = {
 'subsample':[i/100.0 for i in range(75,90,5)],
 'colsample_bytree':[i/100.0 for i in range(75,90,5)]
}

gsearch5 = GridSearchCV(estimator = XGBClassifier( learning_rate =0.1, n_estimators=177, max_depth=4, min_child_weight=6, gamma=0, subsample=0.8, colsample_bytree=0.8, objective= 'binary:logistic', nthread=4, scale_pos_weight=1,seed=27), param_grid = param_test5, scoring='roc_auc',n_jobs=4,iid=False, cv=5)
gsearch5.fit(train[predictors], train[target])
print(gsearch5.cv_results_, gsearch5.best_params_, gsearch5.best_score_)

#正则化参数调优，降低过拟合
#gamma，n_estimators，max_depth 和 min_weight ，subsample ，colsample_bytree取上一步的最优值
param_test6 = {
    'reg_alpha': [1e-5, 1e-2, 0.1, 1, 100]
}
gsearch6 = GridSearchCV(estimator=XGBClassifier(learning_rate=0.1, n_estimators=177, max_depth=4,
                                                min_child_weight=6, gamma=0.1, subsample=0.8, colsample_bytree=0.8,
                                                objective='binary:logistic', nthread=4, scale_pos_weight=1, seed=27),
                        param_grid=param_test6, scoring='roc_auc', n_jobs=4, iid=False, cv=5)
gsearch6.fit(train[predictors], train[target])
print(gsearch6.cv_results_, gsearch6.best_params_, gsearch6.best_score_)

param_test7 = {
    'reg_alpha': [0, 0.001, 0.005, 0.01, 0.05]
}
gsearch7 = GridSearchCV(estimator=XGBClassifier(learning_rate=0.1, n_estimators=177, max_depth=4,
                                                min_child_weight=6, gamma=0.1, subsample=0.8, colsample_bytree=0.8,
                                                objective='binary:logistic', nthread=4, scale_pos_weight=1, seed=27),
                        param_grid=param_test7, scoring='roc_auc', n_jobs=4, iid=False, cv=5)
gsearch7.fit(train[predictors], train[target])
print(gsearch7.cv_results_, gsearch7.best_params_, gsearch7.best_score_)

#将正则化参数引入xgb

xgb3 = XGBClassifier(
    learning_rate=0.1,
    n_estimators=1000,
    max_depth=4,
    min_child_weight=6,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.005,
    objective='binary:logistic',
    nthread=4,
    scale_pos_weight=1,
    seed=27)
modelfit(xgb3, train, test, predictors)