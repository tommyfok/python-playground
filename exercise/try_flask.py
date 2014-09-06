#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '您TMD正在访问首页哦'

@app.route('/signin', methods=['GET'])
def signinPage():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">注册</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return 'Hello 尼玛'
    else:
        return '密码不正确是你的致命伤啊卧槽'

if __name__ == '__main__':
    app.run()
