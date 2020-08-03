# Made by Fabian 13.12.2019
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import statistics
import time
from tqdm import trange
from tqdm import tqdm
from os import system as s
s('cls')

data = pd.read_csv("hotels.csv")

if len(data['quadratmeter']) != len(data['preis']):
    print('Ups es ist was schief gelaufen daten stimmen nicht überein!!')
    exit()

print('Hier sind die Daten veranschaulicht')
print('Einfach das Bild schliessen um weiter zu machen')
plt.scatter(data["preis"], data["quadratmeter"], color='red')
plt.show()

s('cls')

print('Jetzt werden die Anfangspunkte ausgerechnet...')
time.sleep(1)
# y = m * x + b     m, b herausfinden (model.fit)
# Init the function:
# find the nearest x, y coordinates to 0 and the fartest

nearest = None
fartest = None
d_max = None
d_min = None

for i in range(len(data['quadratmeter'])):
    x = data['preis'][i]
    y = data['quadratmeter'][i]
    # distance to 0 with pythagoras:
    # a^2 + b^2 = c^2  ==>  d^2 = x^2 + y^2
    d = math.sqrt(x**2+y**2)
    if nearest == None:
        nearest = (x, y)
        fartest = (x, y)
        d_min = d
        d_max = d
    elif d_min > d:
        nearest = (x, y)
        d_min = d
    elif d_max < d:
        fartest = (x, y)
        d_max = d
    else:
        pass # in between

x1 = nearest[0]
y1 = nearest[1]
x2 = fartest[0]
y2 = fartest[1]

print('Nähester Punkt:', nearest)
print('Entferntester Punkt:', fartest)
time.sleep(.5)
print('Hier sind die nähesten/ entferntesten Punkte markiert.')
print('Einfach das Bild schliessen um weiter zu machen')
plt.scatter(data["preis"], data["quadratmeter"], color='red')
plt.scatter(x1, y1, color='green')
plt.scatter(x2, y2, color='green')
plt.show()

s('cls')

print('Jetzt werden m und b für die Anfangslinie ausgerechnet...')
time.sleep(1)

# find out what m and b is
m = (y2-y1) / (x2-x1)
# y = mx + b umformen und für x, y die nähesten zwei punkte zu nullstelle einsetzen
b = -(m * x1 - y1)

print('Die Anfangsgerade lautet: y = {}x + {}'.format(m, b))

print('Hier ist die Gerade zu denn Daten gezeichnet.')
print('Einfach das Bild schliessen um weiter zu machen')
plt.scatter(data["preis"], data["quadratmeter"], color='r')
plt.scatter(x1, y1, color='green')
plt.scatter(x2, y2, color='green')
plt.plot(data['preis'], data['preis']*m + b, color='b', label='InitLine')
plt.show()

s('cls')

# try to minimize the error
# numpy linearRegression: slope, intercept = np.polyfit(X, Y, 1)

xmean = statistics.mean(data['preis'])
ymean = statistics.mean(data['quadratmeter'])

m1 = 0
m2 = 0

print('Jetzt wird die gerade angepasst...')

for i, x in enumerate(tqdm(list(data['preis']))):
    m1 += (x - xmean) * (data['quadratmeter'][i] - ymean)
    m2 += (x - xmean)**2

    m = m1 / m2

    b = ymean - m * xmean

    plt.scatter(data["preis"], data["quadratmeter"], color='r')
    plt.plot(data['preis'], data['preis']*m + b, color='b')
    plt.show(block=False)
    plt.pause(.05)
    plt.cla()

s('cls')

print('Die perfekte Linie wurde ausgerechenet!')
print('Die perfekte Linie lautet: f(x) = {}x + {}'.format(m, b))
print('Oder auch y = {}x + {}'.format(m, b))
print('Die Finale Gerade wurde gefunden!')
print('Einfach das Bild schliessen um weiter zu machen')
plt.scatter(data["preis"], data["quadratmeter"], color='r')
plt.plot(data['preis'], data['preis']*m + b, color='b', label='FittetLine')
plt.show()

'''
Init the function:
m = (y2-y1) / (x2-x1)
y - y1 = m * (x - x1)  # m * x1 = b
minimize loss:
m = (sum((x-xmean)*(y-ymean)))/sum(x-xmean)
b = ymean - m * xmean

mean = durschnitt von datenpunkten
'''
# Predict the a value:
# f(x) = mx + b => einsetzen
# print(m*20 + b)
s('cls')
print('Jetzt kann man das Program nutzen um vorraussagen zu treffen...')
while True:
    try:
        frage = int(input('Geben sie eine Grösse eines Hotels ein um denn vorrausgesagten Preis zu bekommen: '))
        print('Die KI hat denn preis = {} Euro vorrausgesagt.'.format(m * frage + b))
    except:
        print('Bitte nur Zahlen eingeben, ohne "m" oder änliches!', e)
