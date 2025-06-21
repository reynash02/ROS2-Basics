from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_pub',
            arguments=[
                '0', '0', '1',     # x, y, z
                '0', '0', '0', '1', # qx, qy, qz, qw
                'world',           # frame_id
                'mystaticturtle'   # child_frame_id
            ]
        )
    ])
