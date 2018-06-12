# coding:utf-8
import numpy as np
import pandas as pd
import codecs
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
import spider_city
from flask import Flask
from flask import request
from flask import make_response, Response
import json

app = Flask(__name__)

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

lr = joblib.load("C:\Users\Administrator\PycharmProjects\knn-exp\model/rf.model")
spider = spider_city.Spider()

@app.route('/')
def hello_world():
    return 'hello world'


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/predict', methods=['GET'])
def predict():
    if request.method == 'GET':
        # POST:
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.form.to_dict().get("xxx","")获得
        # ----------------------------------------------------
        # GET:
        # request.args获得所有get参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.args.to_dict().get('xxx',"")获得
        datax = request.args.to_dict()
        area = datax['area'].encode("utf-8")
        area = area_dict[area]
        month = int(datax['month'])
        day =int(datax['day'])
        hour = int(datax['hour'])
        result =spider.find_sec();
        X =[month,day,hour,area,result[area]]
        predict_Y = lr.predict([X])[0]
        content = str("AQI:{}".format(str(predict_Y)))
        resp = Response_headers(content)
        return resp
    else:
        content = json.dumps({"error_code": "1001"})
        resp = Response_headers(content)
        return resp


@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    # resp = Response(content)
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp = Response_headers(content)
    return resp
    # return "error_code:400"


@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp


if __name__ == '__main__':
    app.run(debug=True, threaded=True)