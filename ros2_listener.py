import os

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

TOPIC = os.getenv("TOPIC", '/switches')

class Listener(Node):
    def __init__(self, callback):
        super.__init__('hardware_controller_listener')
        self.callback = callback
        self.subscription = self.create_subscription(String,'topic',self._listener_callback,10)
        self.subscription  # prevent unused variable warning
    
    def _listener_callback(self, msg):
        data = msg.data
        servo = data[:2]
        direction = data[2]
        self.callback(servo, direction)

    def listen(self):
        rclpy.spin(self)
        self.destroy_node()
        rclpy.shutdown()
        