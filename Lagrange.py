import matplotlib.pyplot as plt
import numpy as np

def w_(x, args):
    res = 1
    for i in range(len(args)-1):
        res = res * (x - args[i])
    return res

def excludedMul(i, args):
    res = 1
    for j in range(len(args)):
        if j != i:
            res = res * (args[i] - args[j])
    return res

def separatedDifference(sinput):
    args = sinput[0]
    f = sinput[1]
    res = 0

    for i in range(len(args)):
        res = res + f[i]/excludedMul(i, args)
    return res

def newton(x, dots):
    dots = [[dots[j][i] for j in range(len(dots))] for i in range(len(dots[0]))]

    res = 0
    args = dots[0]
    f = dots[1]
    sinput = [[],[]]
    for i in range(len(args)):
        sinput[0].append(args[i])
        sinput[1].append(f[i])
        res = res + separatedDifference(sinput)*w_(x, sinput[0])
    return res

def kroneker(x, args, i):
    res = 1
    for j in range(len(args)):
        if j != i :
            res = res * (x - args[j])/(args[i] - args[j])
    return res

def lagrange(x, dots):
    dots = [[dots[j][i] for j in range(len(dots))] for i in range(len(dots[0]))]

    res = 0
    args = dots[0]
    f = dots[1]

    for i in range(len(args)):
        res = res + f[i]*kroneker(x, args, i)
    
    return res

def sortKey(arr):
    return arr[0]

def main():
    raw = input("Write down points in x,y x,y x,y format. For example 1,1 2,2 3,1: ")
    raw = raw.split()

    for i in range(len(raw)):
        row = raw[i].split(',')
        for j in range(len(row)):
            row[j] = int(row[j])

        raw[i] = row

    print(raw)
    raw.sort(key = sortKey)
    print(raw)

    dots = raw

    dotsTransposed = [[dots[j][i] for j in range(len(dots))] for i in range(len(dots[0]))]

    x = []
    y = []
    for i in range(101):
        x.append((dotsTransposed[0][-1]-dotsTransposed[0][0])/100*i+dotsTransposed[0][0])
    
    for i in x:
        y.append(lagrange(i, dots))

    p = plt.figure("Lagrange")
    plt.plot(x, y, 'c')
    plt.plot(dotsTransposed[0], dotsTransposed[1], 'o')
    p.text(0, 0, "Ln(2,5) = " + str(lagrange(2.5, dots)))

#   Часть кода которая строит график методом Ньютона
#    y = []
#
#    for i in x:
#        y.append(newton(i, dots))
#
#    p = plt.figure("Newton")
#    plt.plot(x, y, 'g')
#    plt.plot(dotsTransposed[0], dotsTransposed[1], 'o')
#    p.text(0, 0, "Ln(2,5) = " + str(newton(2.5, dots)))


    plt.show()

main()


