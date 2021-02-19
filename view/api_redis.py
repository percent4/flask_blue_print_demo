# -*- coding: utf-8 -*-
# @Time : 2021/2/9 17:18
# @Author : Jclian91
# @File : api_redis.py
# @Place : Yangpu, Shanghai
from flask import Blueprint

api_redis = Blueprint('app_redis', __name__, url_prefix="/redis")


@api_redis.route('/show')
def show():
    return "Hello from Redis!"
