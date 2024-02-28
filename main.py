from colour import *

def numbers(number):
    try:
        return red(number + 2)
    except TypeError:
        return red("Qabul qilingan raqam - raqam emas!")
