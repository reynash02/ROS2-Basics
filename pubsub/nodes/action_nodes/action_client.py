#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from pubsub.action import Fib

class FibClient(Node):
    def __init__(self):
        super().__init__('fib_client')
        self.action_client=ActionClient(self, Fib, 'fib')
    
    def send_goal(self, order):
        goal_msg=Fib.Goal()
        goal_msg.order=order
        self.action_client.wait_for_server()
        self.send_goal_future=self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle=future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Rejected Goal')
            return
        self.get_logger().info('Goal Accepted')
        self.get_result_future=goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result=future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback=feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))

def main(args=None):
    rclpy.init(args=args)
    node=FibClient()
    node.send_goal(10)
    rclpy.spin(node)

if __name__=='__main__':
    main()
