#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from scipy.spatial.transform import Rotation as R
from math import cos, sin

class TFBroadcasterNode(Node):
    def __init__(self):
        super().__init__('broadcaster_node')
        self.get_logger().info("Started broadcaster node (circular TF)")
        self.broadcaster = TransformBroadcaster(self)

        # Parameters
        self.angle1 = 0.0
        self.angle2 = 3.14 / 4
        self.radius = 1.0
        self.delta_angle = 0.05

        self.timer = self.create_timer(0.1, self.broadcast_tf)

    def broadcast_tf(self):
        now = self.get_clock().now().to_msg()

        # First Transform
        t1 = TransformStamped()
        t1.header.stamp = now
        t1.header.frame_id = 'base_link'
        t1.child_frame_id = 'first_link'
        t1.transform.translation.x = self.radius * cos(self.angle1)
        t1.transform.translation.y = self.radius * sin(self.angle1)
        t1.transform.translation.z = 0.0

        q1 = R.from_euler('z', 5 * self.angle1).as_quat()
        t1.transform.rotation.x = q1[0]
        t1.transform.rotation.y = q1[1]
        t1.transform.rotation.z = q1[2]
        t1.transform.rotation.w = q1[3]

        # Second Transform
        t2 = TransformStamped()
        t2.header.stamp = now
        t2.header.frame_id = 'base_link'
        t2.child_frame_id = 'second_link'
        t2.transform.translation.x = self.radius * cos(self.angle2)
        t2.transform.translation.y = self.radius * sin(self.angle2)
        t2.transform.translation.z = 0.0

        q2 = R.from_euler('z', 5 * self.angle2).as_quat()
        t2.transform.rotation.x = q2[0]
        t2.transform.rotation.y = q2[1]
        t2.transform.rotation.z = q2[2]
        t2.transform.rotation.w = q2[3]

        # Broadcast both transforms
        self.broadcaster.sendTransform(t1)
        self.broadcaster.sendTransform(t2)

        # Update angles
        self.angle1 += self.delta_angle
        self.angle2 += self.delta_angle

        self.get_logger().info("TF messages broadcasted")

def main(args=None):
    rclpy.init(args=args)
    node = TFBroadcasterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
