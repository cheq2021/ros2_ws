from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_autoware',
            executable='initialpose',
            name='py_autoware',
            output='screen',
            emulate_tty=True,
            # for carla town01
            parameters=[
                {'position_x': 310.2},
                {'position_y': -129.2},
                {'position_z': 0.0},
                {'orientation_x': 0.0},
                {'orientation_y': 0.0},
                {'orientation_z': -0.999},
                {'orientation_w': 0.0224},
            ]
        )
    ])
# point
                # {'init_x': 1.6},
                # {'init_y': -149.8}