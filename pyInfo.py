# # import requests
# #
# #
# # def get_info():
# #     pass
# from turtle import *
# from time import *
# import turtle
# t = Turtle()
# t.pensize(2)
# turtle.bgcolor("black")
# colors = ["red", "yellow", 'purple', 'blue']
# t._tracer(False)
# # for x in range(400):
# #     t.forward(2*x)
# #     t.color(colors[x % 4])
# #     t.left(91)
# # t._tracer(True)
# done()
import re
import hashlib
def get_info(moudle,collpase):
    #得到模块的方法
    methods = [x for x in dir(moudle) if callable(getattr(moudle,x))]
    formatter =  collpase and(lambda x : x) or (lambda x : " ".join(x.split()))
    #打印出左边是方法名 ， 右边是文档
    print("\n".join(['%s %s'%(method.ljust(20),formatter(str(getattr(moudle,method).__doc__))) for method in methods]))
get_info(hashlib,20)