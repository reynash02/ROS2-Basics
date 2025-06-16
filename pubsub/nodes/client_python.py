#!/usr/bin/env python3
import sys
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class ServicePython(Node):
    def __init__(self):
        super().__init__('client')   # initializes node with name client
        self.cli=self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service")
        self.req=AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a=a
        self.req.b=b
        self.future=self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main():
    rclpy.init()
    if len(sys.argv) < 3:
        print("Usage: ros2 run pubsub client_python.py <a> <b>")
        return

    node = ServicePython()
    response = node.send_request(int(sys.argv[1]), int(sys.argv[2]))
    node.get_logger().info('Result of %d + %d = %d' % (int(sys.argv[1]), int(sys.argv[2]), response.sum))
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()