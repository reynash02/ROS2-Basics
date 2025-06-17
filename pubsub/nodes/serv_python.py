#!/usr/bin/env python3

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class ServicePython(Node):
    def __init__(self):
        super().__init__('service')   # initializes node with name service
        self.srv=self.create_service(AddTwoInts, 'add_two_ints', self.service_callback) # will call the method service_callback whenever a request is received

    def service_callback(self, req, response):   # callback function that handles incoming service requests
        response.sum=req.a+req.b    # Compute the sum of the two integers from the request
        self.get_logger().info('Incoming request\na: %d b: %d' % (req.a,req.b))
        return response

def main(args=None):
    rclpy.init(args=args)   #initialise ros2 python interface
    node=ServicePython()    #create instance
    rclpy.spin(node)    #keep the node listening for events
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()