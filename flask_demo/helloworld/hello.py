# -*- coding: utf-8 -*-
# @Time : 2018/8/12 20:08
# @File : hello.py
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/sxr/')
def hello_world():
    name = request.args.get('name')
    idnum = request.args.get('idnum')
    print(name)
    print(idnum)
    return str(name)+str(idnum)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')