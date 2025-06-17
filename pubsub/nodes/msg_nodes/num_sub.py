#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from pubsub.msg import Num 

class NumSubscriber(Node):
    def __init__(self):
        super().__init__('num_subscriber')
        self.subscription = self.create_subscription(Num, '/num', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.num}')

def main(args=None):
    rclpy.init(args=args)
    node=NumSubscriber()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
