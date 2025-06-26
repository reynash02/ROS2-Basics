import launch
import os
import launch_ros
from launch.substitutions import LaunchConfiguration, Command

package_name='urdf_tutorials'
urdf_path='urdf/r2d2.urdf'

def generate_launch_description():
    pkg_path=launch_ros.substitutions.FindPackageShare(package=package_name).find(package_name)
    model_path=os.path.join(pkg_path, urdf_path)
    print(model_path)

    with open(model_path, 'r') as infp:
        robot_desc=infp.read()
    
    params={'robot_description':robot_desc}
    robot_state_publisher_node=launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params],
        arguments=[model_path]
    )
    rviz_node=launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return launch.LaunchDescription([
        robot_state_publisher_node,
        rviz_node
    ])