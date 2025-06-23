from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('tf2_package'), 'launch', 'listener.launch.py'])
        ),
        Node(
            package='tf2_package',
            executable='adding_fixed_frame.py',
            name='fixed_broadcaster',
        ),
    ])