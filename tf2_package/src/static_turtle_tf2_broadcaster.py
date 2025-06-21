#!/usr/bin/env python3
#not working

import rclpy.logging
from rclpy.node import Node
import math, sys
from geometry_msgs.msg import TransformStamped  # provides us a template for the message that we will publish to the transformation tree.
import numpy as np
import rclpy
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster

def quaternion_from_euler(ai, aj, ak):
    ai/=2.0
    aj/=2.0
    ak/=2.0
    ci=math.cos(ai)
    si=math.sin(ai)
    cj=math.cos(aj)
    sj=math.sin(aj)
    ck=math.cos(ak)
    sk=math.sin(ak)
    cc=ci*ck
    cs=ci*sk
    sc=si*ck
    ss=si*sk

    q=np.empty((4, ))
    q[0]=cj*sc-sj*cs
    q[1]=cj*ss+sj*cc
    q[2]=cj*cs-sj*sc
    q[3]=cj*cc+sj*ss
    return q

class StaticPublisher(Node):       #this example publishes transforms from `world` to a static turtle frame
    def __init__(self, transformation):  #The transforms are only published once at startup, and are constant for all time
        super().__init__('static_turtle_tf2_broadcaster')
        self.tf_static=StaticTransformBroadcaster(self)     # will send one static transformation upon the startup
        self.make_transforms(transformation)

    def make_transforms(self, transformation):
        t=TransformStamped()    # message to be sent
        t.header.stamp=self.get_clock().now().to_msg()
        t.header.frame_id='world'   #parent frame
        t.child_frame_id=transformation[1]  #child frame
        t.transform.translation.x=float(transformation[2])
        t.transform.translation.y=float(transformation[3])
        t.transform.translation.z=float(transformation[4])

        quat=quaternion_from_euler(float(transformation[5]), float(transformation[6]), float(transformation[7]))

        t.transform.rotation.x=quat[0]
        t.transform.rotation.y=quat[1]
        t.transform.rotation.z=quat[2]
        t.transform.rotation.w=quat[3]

        self.tf_static.sendTransform(t)

def main(args=None):
    logger=rclpy.logging.get_logger('logger')
    if len(sys.argv)!=8:
        logger.info('Invalid number of parameters. Usage: \n'
                    '$ ros2 run learning_tf2_py static_turtle_tf2_broadcaster'
                    'child_frame_name x y z roll pitch yaw')
        sys.exit(1)
    
    if sys.argv[1]=='world':
        logger.info('Your static turtle name cannot be "world"')
        sys.exit(2)

    rclpy.init()
    node=StaticPublisher(sys.argv)
    
    # Add this to keep node alive
    logger.info("Publishing static transform. Press Ctrl+C to exit.")
    rclpy.spin(node)
    
    rclpy.shutdown()