# -*- coding: utf-8 -*-
# @Time : 2021/2/9 16:57
# @Author : Jclian91
# @File : main.py
# @Place : Yangpu, Shanghai
from flask import Flask, Blueprint
from view.api import app2
from view.api_redis import api_redis

app = Flask(__name__)
app.register_blueprint(app2)
app.register_blueprint(api_redis)


@app.route('/')
def index():
    return "Hello index"


@app.route('/test')
def test():
    return "Hello test"


if __name__ == '__main__':
    # 获取所有请求的URL路径
    print("-->", app.url_map.__repr__())
    app.run(host="0.0.0.0", port=5000, debug=True)
