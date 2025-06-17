#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from pubsub.msg import Sphere

class SpherePublisher(Node):
    def __init__(self):
        super().__init__('sphere_publisher')
        self.pub=self.create_publisher(Sphere, '/sphere', 10)
        self.timer=self.create_timer(1.0, self.publish_sphere)
        self.get_logger().info('Sphere publisher started')

    def publish_sphere(self):
        msg=Sphere()
        msg.center=Point(x=2.0, y=-1.0, z=3.0)
        msg.radius=5.0
        self.pub.publish(msg)
        self.get_logger().info(f'Published Sphere: center=({msg.center.x}, {msg.center.y}, {msg.center.z}), radius={msg.radius}')

def main(args=None):
    rclpy.init(args=args)
    node=SpherePublisher()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
