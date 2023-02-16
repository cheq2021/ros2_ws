from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_autoware',
            executable='initialgoal',
            name='py_autoware',
            output='screen',
            emulate_tty=True,
            # for carla town01
            parameters=[
                {'position_x': 195.1619110107422},
                {'position_y': -128.7124481201172},
                {'position_z': 0.0},
                {'orientation_x': 0.0},
                {'orientation_y': 0.0},
                {'orientation_z': -0.9992380026160627},
                {'orientation_w': 0.03903093808585461},
            ]
        )
    ])
# point
                # {'init_x': 1.6},
                # {'init_y': -149.8}