#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber')   # initializes node with name subscriber
        self.sub=self.create_subscription(String, 'communication', self.listener_callback, 10)
        self.sub

    def listener_callback(self, msg):
        self.get_logger().info("Received: %s" %msg.data)

def main(args=None):
    rclpy.init(args=args)   #initialise ros2 python interface
    node=SubscriberNode()    #create instance
    rclpy.spin(node)    #keep the node listening for events
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()