#!/usr/bin/python
"""
@brief Run QuickBot class for Beaglebone Black

@author Rowland O'Flaherty (rowlandoflaherty.com)
@date 02/07/2014
@version: 1.0
@copyright: Copyright (C) 2014, Georgia Tech Research Corporation see the LICENSE file included with this software (see LINENSE file)
"""

import sys
import time


import Adafruit_BBIO.ADC as ADC
import numpy as np

if __name__ == '__main__':
    """
	import config

    NUM_SAMPLES = 10 # 5-10 seconds of data

    size = NUM_SAMPLES
    buf = np.zeros((size, len(config.ENC_PINS)), dtype=np.int)

  
    ADC.setup()

    for i in range(size):
 	values = tuple(ADC.read_raw(pin) for pin in config.ENC_PINS)
        print('Raw encoder values: %4d  %4d' % values)
        buf[i, 0] = values[0]
        buf[i, 1] = values[1]
        time.sleep(0.001)

    print "Done"
"""



from QuickBot import *

print "Running QuickBot"

baseIP = '192.168.1.101'
robotIP = '192.168.1.100'

if len(sys.argv) > 3:
    print 'Invalid number of command line arguments.'
    print 'Proper syntax:'
    print '>> QuickBotRun.py baseIP robotIP'
    print 'Example:'
    print '>> QuickBotRun.py ', baseIP, ' ', robotIP
    sys.exit()

if len(sys.argv) >= 2:
    baseIP = sys.argv[1]

if len(sys.argv) >= 3:
    robotIP = sys.argv[2]

print 'Running QuickBot Program'
print '    Base IP: ', baseIP
print '    Robot IP: ', robotIP

ADC.setup()

QB = QuickBot(baseIP, robotIP)
QB.run()
