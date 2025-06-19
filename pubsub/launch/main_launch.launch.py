from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

def generate_launch_description():
    colors={'background_r': '200'}  # Dictionary to hold color settings and red component of the background color
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('pubsub'), 'launch', 'sub_launch.launch.py'  # Include another launch file from the 'pubsub' package
                ])
            ]),
            launch_arguments={
                'turtlesim_ns': 'turtlesim2',  # Namespace for turtlesim node
                'use_provided_red': 'True',
                'new_background_r': TextSubstitution(text=str(colors['background_r']))
            }.items()

        )
    ])