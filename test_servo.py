#!/usr/bin/env python3

import sys

import busio
import board

from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = PWM_FREQ

channel = int(sys.argv[1])
duty_cycle =float(sys.argv[2])

pca.channels[channel].duty_cycle = int(duty_cycle*65535)