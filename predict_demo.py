#!/usr/bin/env python
# encoding: utf-8
'''
@author: agandong4
@license: (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
@contact: agandong4@gmail.com
@software: garner
@file: stock_market.py
@time: 2019-04-24 22:13
@desc:
'''
# from config import token
import tushare as ts
# ts.set_token(token)
# pro = ts.pro_api()
import datetime
from sklearn.linear_model import LinearRegression




def main():
    today = datetime.date.today()
    delta = datetime.timedelta(days=30)
    data = ts.get_hist_data("600036",start=str(today-delta),end=str(today))
    # print(data)
    xtrain = []
    ytrain = []

    for i in range(1,data.shape[0]):
        tmp = []
        tmp.append(data.iloc[i]['open'])
        tmp.append(data.iloc[i]['high'])
        tmp.append(data.iloc[i]['close'])
        tmp.append(data.iloc[i]['low'])
        xtrain.append(tmp)
        tmp2 = (data.iloc[i]['close']-data.iloc[i]['open'])/data.iloc[i]['open']
        ytrain.append(tmp)

    xtest = xtrain[:1]

    # print(xtrain.shape())
    # print(ytrain.shape())

    linreg = LinearRegression()
    linreg.fit(xtrain,ytrain)

    ypred = linreg.predict(xtest)

    print(ypred)

if __name__ == '__main__':
    main()