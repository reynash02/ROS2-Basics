#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from pubsub.action import Fib
from rclpy.action import ActionServer
import time

class FibServer(Node):
    def __init__(self):
        super().__init__('fib_server')
        self.action_server=ActionServer(self, Fib, 'fib', self.execute_callback)
    
    async def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal')
        feedback_msg=Fib.Feedback()
        feedback_msg.partial_sequence=[0,1]
        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(feedback_msg.partial_sequence[i]+feedback_msg.partial_sequence[i-1])
        self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
        goal_handle.publish_feedback(feedback_msg)
        time.sleep(1)

        goal_handle.succeed()
        result=Fib.Result()
        result.sequence=feedback_msg.partial_sequence
        return result

    

def main(args=None):
    rclpy.init(args=args)
    node=FibServer()
    rclpy.spin(node)

if __name__=='__main__':
    main()
