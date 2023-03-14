from random import choices
import json
import os
from alive_progress import alive_bar
import matplotlib.pyplot as plt


def programInitialize():
    testMode = False
    mainDir = 'C:\Coding Projects1\Bernsley Fern\Affline Permutations'
    if testMode == False:
        for i in range(0, len(os.listdir(mainDir))): 
            print('['+str(i)+'] '+os.listdir(mainDir)[i])        
        fNum = input('Choose a File: ')
    else:
        fNum = 0

    # Initializes json into a dictionary
    directory = os.path.join(mainDir, os.listdir(mainDir)[int(fNum)])
    with open(directory, 'r') as j:
        funcDict = json.load(j, parse_float = lambda x: float(x))

    global weights
    global values
    weights = []
    values = []

    for i in funcDict:
        weights.append(funcDict[i]['p'])
        values.append(funcDict[i])   

    if testMode == False:
        pltNum = int(input('how many recursions?   '))
    else:
        pltNum = 10

    return pltNum

def transform(x, y):
    func = (choices(values, weights))[0]
    xn = x * func['a'] + y * func['b'] + func['e']
    yn = y * func['c'] + y * func['d'] + func['f']
    c = func['p']*100
    return (xn, yn)

def recursion(recNum):
    pList = [[], []]
    v = transform(0, 0)
    with alive_bar(recNum) as bar:
        for i in range(recNum):
            for n in range(0, len(pList)):
                pList[n].append(v[n])
            v = transform(v[0], v[1])
            bar()
    return pList



def scatterPlot(pltNum):

    plt.ion()
    fig, ax = plt.subplots()
    init_rec = 1
    x, y = recursion(init_rec)
    sc = ax.scatter(x,y)
    plt.draw()

    for i in range(pltNum):
        x, y = recursion(1*10**i)
        sc = ax.scatter(x,y, s=1, c='c')
        fig.canvas.draw_idle()
        ax.set_title('# of points = ' + str(1*10**i))
        plt.pause(1.5)
    
    plt.waitforbuttonpress()


pltNum = programInitialize()
scatterPlot(pltNum)



    
