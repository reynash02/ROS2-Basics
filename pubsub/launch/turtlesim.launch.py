from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
    return LaunchDescription([
        Node(package="turtlesim",
             namespace="turtlesim1",
             executable="turtlesim_node",
             output="screen"
            ),

        Node(package="turtlesim",
             namespace="turtlesim2",
             executable="turtlesim_node",
             output="screen"
        ),

        Node(package="turtlesim",
             name="mimic",
             executable="mimic",
            output="screen",
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel')]
        )
    ])