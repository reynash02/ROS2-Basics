#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from pubsub.srv import Addthreeints

class AddThreeIntsClient(Node):
    def __init__(self):
        super().__init__('add_three_ints_client')
        self.client=self.create_client(Addthreeints, 'add_three_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
        self.request=Addthreeints.Request()
        self.send_request()

    def send_request(self):
        self.request.a=10
        self.request.b=20
        self.request.c=30
        future=self.client.call_async(self.request)
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response=future.result()
            self.get_logger().info(f"Result: {response.sum}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node=AddThreeIntsClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
