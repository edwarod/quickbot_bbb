import Adafruit_BBIO.GPIO as GPIO
import time

a=0
b=0

def derecha(channel):
  global a
  a+=1
  print 'cuenta derecha es {0}'.format(a)
  

def izquierda(channel):
  global b
  b+=1
  print 'cuenta izquierda es {0}'.format(b)

GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.add_event_detect("P9_11", GPIO.BOTH)
GPIO.add_event_detect("P9_13", GPIO.BOTH)
GPIO.add_event_callback("P9_11",derecha)
GPIO.add_event_callback("P9_13",izquierda)



#if GPIO.event_detected("GPIO_31"):
#  print "event detected"

while True:
  print "cosas pasan"
  time.sleep(1)
