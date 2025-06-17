#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from pubsub.srv import Addthreeints

class AddThreeIntsServer(Node):
    def __init__(self):
        super().__init__('add_three_ints_server')
        self.srv=self.create_service(Addthreeints, 'add_three_ints', self.add_three_ints_callback)
        self.get_logger().info('Service server ready.')

    def add_three_ints_callback(self, request, response):
        response.sum=request.a+request.b+request.c
        self.get_logger().info(f"Received: a={request.a}, b={request.b}, c={request.c} => sum={response.sum}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node=AddThreeIntsServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
