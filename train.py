# coding:utf-8
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np;
import pandas as pd
import codecs
from sklearn.externals import joblib

area_dict = {
    '东四': 1,
    '天坛': 2,
    '官园': 3,
    '万寿西宫': 4,
    '奥体中心': 5,
    '农展馆': 6,
    '万柳': 7, '北部新区': 8, '植物园': 9
    , '丰台花园': 10, '云岗': 11, '古城': 12
    , '房山': 13, '大兴': 14, '亦庄': 15, '通州': 16, '顺义': 17
    , '昌平': 18, '门头沟': 19, '平谷': 20, '怀柔': 21, '密云': 22,
    '延庆': 23, '定陵': 24, '八达岭': 25, '密云水库': 26, '东高村': 27
    , '永乐店': 28, '榆垡': 29,
    '琉璃河': 30, '前门': 31, '永定门内': 32,
    '西直门北': 33, '南三环': 34, '东四环': 35
}


def load_data():
    train_df = pd.read_csv("C:\Users\Administrator\PycharmProjects\knn-exp/train_data/beijing_train.csv")
    label = train_df.pop('label')
    return np.array(train_df), label;


X, y = load_data();

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

lr = LinearRegression()

lr.fit(X_train, y_train)

lr_y_predict = lr.predict(X_test)

print 'The value of default measurement of LinearRegression is: ', lr.score(X_test, y_test)

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

print 'The value of R-squared of LinearRegression is: ', r2_score(y_test, lr_y_predict)

# save model
joblib.dump(lr,'C:\Users\Administrator\PycharmProjects\knn-exp\model/rf.model')