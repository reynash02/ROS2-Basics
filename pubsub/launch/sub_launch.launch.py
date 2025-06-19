from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution

def generate_launch_description():
    turtlesim_ns = LaunchConfiguration('turtlesim_ns')  #namespace for turtlesim node
    use_provided_red = LaunchConfiguration('use_provided_red')  # Whether to use provided red value
    new_background_r = LaunchConfiguration('new_background_r')  # New background red value
    
    turtlesim_ns_launch_arg = DeclareLaunchArgument(
        'turtlesim_ns',
        default_value='turtlesim1'
    )
    
    use_provided_red_launch_arg = DeclareLaunchArgument(
        'use_provided_red',
        default_value='False'
    )
    
    new_background_r_launch_arg = DeclareLaunchArgument(
        'new_background_r',
        default_value='200'
    )
    
    turtlesim_node = Node(      # Launch the turtlesim node
        package='turtlesim',
        executable='turtlesim_node',
        namespace=turtlesim_ns,
        name='sim',
        parameters=[{'background_r': 120}]
    )
    
    spawn_turtle = ExecuteProcess(  # Execute a process to spawn a new turtle at position (2.0, 2.0) with angle 0.2
        cmd=[
            'ros2', 'service', 'call',
            PathJoinSubstitution([turtlesim_ns, 'sim', 'spawn']),
            'turtlesim/srv/Spawn',
            '{"x": 2.0, "y": 2.0, "theta": 0.2}'
        ],
        shell=False
    )
    
    change_background_r = ExecuteProcess(   # Set background red parameter to 120
        cmd=[
            'ros2', 'param', 'set',
            PathJoinSubstitution([turtlesim_ns, 'sim']),
            'background_r',
            '120'
        ],
        shell=False
    )
    
    change_background_r_conditioned = ExecuteProcess(   # Conditionally set the background red value
        condition=IfCondition(
            PythonExpression([
                new_background_r,
                ' == 200',
                ' and ',
                use_provided_red
            ])
        ),
        cmd=[
            'ros2', 'param', 'set',
            PathJoinSubstitution([turtlesim_ns, 'sim']),
            'background_r',
            new_background_r
        ],
        shell=False
    )
    
    return LaunchDescription([
        turtlesim_ns_launch_arg,
        use_provided_red_launch_arg,
        new_background_r_launch_arg,
        turtlesim_node,
        TimerAction(
            period=2.0,
            actions=[
                spawn_turtle,
                change_background_r,
                change_background_r_conditioned
            ]
        )
    ])