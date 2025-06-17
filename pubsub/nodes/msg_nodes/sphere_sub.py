#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from pubsub.msg import Sphere

class SphereSubscriber(Node):
    def __init__(self):
        super().__init__('sphere_subscriber')
        self.sub=self.create_subscription(Sphere, '/sphere', self.listener_callback, 10)
        self.get_logger().info('Sphere subscriber started.')

    def listener_callback(self, msg):
        x0, y0, z0 = msg.center.x, msg.center.y, msg.center.z
        r=msg.radius
        sphere_eq=f'(x-{x0})^2+(y-{y0})^2+(z-{z0})^2={r**2}'
        self.get_logger().info(f'Received Sphere. Equation: {sphere_eq}')

def main(args=None):
    rclpy.init(args=args)
    node=SphereSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
