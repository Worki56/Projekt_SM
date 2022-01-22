import serial
import time
import numpy as np
from itertools import count
from threading import Thread
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

stm32 = serial.Serial('COM3', 115200, timeout=0.01)
x=50
esa='40'
n=0
plt.figure()
plt.style.use('fivethirtyeight')
plt.ion()
plt.show()
wyniki=[]
wyniki1=[]
wyniki2=[]
ile=count()
spaw=0
wyraz_tyczas=""
def myfunc():
    fdf=input("Podaj ilość obrotów (2cyfry)\n")
    stm32.write(fdf.encode())
    global n
    n=0
    return

while True:

    data = stm32.readline()
    if data:
        data = data.decode()
        for i in range(0, len(data)):

            if data[i] == " " or data[i] == "\n":
                if spaw==0:
                    wyniki.append(int(wyraz_tyczas))
                    spaw=1
                elif spaw==1:
                    wyniki1.append(int(wyraz_tyczas))
                    spaw=0
                wyraz_tyczas=''
            else:
                wyraz_tyczas = wyraz_tyczas + data[i]
        wyniki2.append(next(ile))
        plt.cla()
        plt.plot(wyniki2[-100:-1],wyniki[-100:-1])
        plt.plot(wyniki2[-100:-1],wyniki1[-100:-1])
        plt.pause(0.01)


    if n==0:
        n = 1
        t = Thread(target=myfunc)
        t.start()













