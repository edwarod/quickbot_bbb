#!/usr/bin/python

import os
import time
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_14", GPIO.IN)

LEFT = 0
RIGHT = 1

size = 100000

# encoderPin = ('P9_39', 'P9_33')
encoderVal = [0, 0]
valList = [0] * size
timeList = [0] * size

runFlag = True

t0 = time.time()

def run():

    cnt = 0
    while runFlag == True and cnt < size:
        t = time.time() - t0
        update()
        valList[cnt] = encoderVal[LEFT]
        timeList[cnt] = t
        cnt = cnt + 1

def update():
    encoderVal[LEFT] = GPIO.input("P8_14")
    # encoderVal[LEFT] = ADC.read(encoderPin[LEFT])
    # encoderVal[RIGHT] = ADC.read_raw(encoderPin[RIGHT])

run()

matrix = map(list, zip(*[timeList, valList]))
s = [[str(e) for e in row] for row in matrix]
lens = [len(max(col, key=len)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
f = open('output.txt','w')
f.write('\n'.join(table))
f.close()
