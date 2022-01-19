b = input("enter function:")

import math

if b == "sin" or "cos" or "tan" or "cot" or "factorial":
    a = float(input("enter number:"))
    if b == "sin":
        d = a * math.pi / 180
        c = math.sin(d)
        result = c

    if b == "cos":
        d = a * math.pi / 180
        c = math.cos(d)
        result = c

    if b == "tan":
        d = a * math.pi / 180
        c = math.tan(d)
        result = c

    if b == "cot":
        d = a * math.pi / 180
        c = math.tan(d)
        p = 1 / c
        result = p

    if b == "factorial":
        d = math.factorial(a)
        result = d

elif b == "+" or "-" or "*" or "/":
    k = float(input("enter 1th number:"))
    e = float(input("enter 2nd number:"))
    if b == "+":
        s = k + e
        

    if b == "-":
        s = k - e
        

    if b == "*":
        s = k * e

    if b == "/":
        s = k / e

    print(s)
