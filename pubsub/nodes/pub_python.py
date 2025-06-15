#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')   # initializes node with name publisher
        self.pub=self.create_publisher(String,'/communication',10)  #creates a publisher with params (msg_type, topic, queue_size)
        self.timer=self.create_timer(0.5, self.timer_callback)
        self.i=0

    def timer_callback(self):
        msg=String()  #create new string message
        msg.data="Hello World: %d" %self.i   #set msg value
        self.pub.publish(msg)    #publish message
        self.get_logger().info("Publishing: %s" %msg.data)    #log message to the terminal
        self.i+=1

def main(args=None):
    rclpy.init(args=args)   #initialise ros2 python interface
    node=PublisherNode()    #create instance
    rclpy.spin(node)    #keep the node listening for events
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()