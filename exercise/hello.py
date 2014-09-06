#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def double(x):
    if not isinstance(x, int):
        return None
    return x * x

myList = [double(x) for x in range(1,100)]
fileList = [x for x in os.listdir('.')]
#print fileList

def app(env, res):
    def test(data):
        return str(data)
    res('200 OK', [('Content-Type', 'text/html')])
    return str(fileList), test('我顶你个肺'), __name__
