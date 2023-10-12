#!/usr/bin/env python3

import time
import os
import yaml
import subprocess

import busio
import board

from adafruit_pca9685 import PCA9685

class Color:
    # ANSI escape sequences for text colors
    RED = '\033[91m'
    BLUE = '\033[94m'  
    END = '\033[0m'
def printe(message):
    print(f"{Color.RED}Error: {message}{Color.END}")
def printi(message):
    print(f"{Color.BLUE}Info: {message}{Color.END}")

PWM_FREQ = os.getenv("PWM_FREQ", 50)

# Connection methods
ROS = os.getenv("ROS", 0)
UDP = os.getenv("UDP", 0) # remember to also set PORT
def get_conn():
    for conn in ['UDP', 'ROS']:
        if os.getenv(conn, 0):
            return conn
    return 'UDP'
CONN = get_conn()

# global vars
config = None
pca = None

"""
servo: 0-15 (16 servos)
direction: left, straight, right
"""
def callback(servo, direction):
    # get pca channel from config
    channel = config[servo]['channel']
    # check if direction is defined in config
    if direction not in config[servo]:
        printe(f"Direction {direction} not defined in config for servo {servo} on channel {channel}")
        return
    # get duty cycle from config
    duty_cycle = config[servo][direction]
    # set duty cycle
    pca.channels[channel].duty_cycle = int(duty_cycle*65535)
    print(f"Setting servo {servo} on channel {channel} to {direction} ({duty_cycle})")

def main():
    global config, pca
    printi(f"Using {CONN} as connection method")
    # load config
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        printi(f"Loaded config with {len(config)} servos")
    if config is None or config == {}:
        printe("Failed to load config")
        return
    # init pca
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = PCA9685(i2c, address=0x41)
    pca.frequency = PWM_FREQ

    # init listener
    listener = None
    if CONN == 'UDP':
        import udp_listener
        listener = udp_listener.Listener(callback)
    elif CONN == 'ROS':
        import ros2_listener
        rclpy.init()
        listener = ros2_listener.Listener(callback)
    
    # this should run a loop that calls callback on incoming messages
    printi("Listening for incoming messages")
    listener.listen()

if __name__ == "__main__":
    main()