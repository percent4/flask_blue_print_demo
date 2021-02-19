# -*- coding: utf-8 -*-
# @Time : 2021/2/9 16:57
# @Author : Jclian91
# @File : api.py
# @Place : Yangpu, Shanghai
from flask import Blueprint

app2 = Blueprint('app2', __name__, url_prefix="/new")


@app2.route('/app2')
def show():
    return "Hello Blueprint app2"
