import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

def generate_launch_description():
    turtlesim_world_1=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('pubsub'),
                         'turtlesim_project'),
                         '/turtlesim_world_1_launch.py'])
    )

    turtlesim_world_2=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('pubsub'),
                'turtlesim_project'),
                '/turtlesim_world_2_launch.py'])
    )

    turtlesim_world_2_with_namespace=GroupAction(
        actions=[
            PushRosNamespace('turtlesim2'),
            turtlesim_world_2,
        ]
    )

    turtlesim_world_3=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('pubsub'),
                'turtlesim_project'),
                '/turtlesim_world_3_launch.py'])
    )

    broadcaster_listener_nodes=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('pubsub'),
                'turtlesim_project'),
                '/broadcaster_listener_launch.py']),
        launch_arguments={'target_frame': 'carrot1'}.items(),
    )

    mimic_node=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('pubsub'),
                'turtlesim_project'),
                '/mimic_launch.py'
        ])
    )

    fixed_frame_node=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('pubsub'),
                'turtlesim_project'),
                '/fixed_broadcaster_launch.py'
        ])
    )

    rviz_node=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('pubsub'),
                'turtlesim_project'),
                '/turtlesim_rviz_launch.py'
        ])
    )

    return LaunchDescription([
        turtlesim_world_1,
        turtlesim_world_2_with_namespace,
        turtlesim_world_3,
        broadcaster_listener_nodes,
        mimic_node,
        fixed_frame_node,
        rviz_node
    ])