#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from pubsub.msg import Num

class NumPublisher(Node):
    def __init__(self):
        super().__init__('num_publisher')   # initializes node with name num_publisher
        self.pub=self.create_publisher(Num,'/num',10)  #creates a publisher with params (msg_type, topic, queue_size)
        self.timer=self.create_timer(1.0, self.timer_callback)
        self.i=0

    def timer_callback(self):
        msg=Num()  #create new string message
        msg.num=self.i
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing: {msg.num}')        
        self.i+=1

def main(args=None):
    rclpy.init(args=args)   #initialise ros2 python interface
    node=NumPublisher()    #create instance
    rclpy.spin(node)    #keep the node listening for events
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()