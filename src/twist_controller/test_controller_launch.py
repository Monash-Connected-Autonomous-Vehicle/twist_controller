from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='twist_controller',
            executable='twist_controller.py',
            name='twist_controller',
            output='screen'
        ),
        Node(
            package='vehicle_interface',
            executable='sd_vehicle_interface.h',
            name='sd_vehicle_interface',
            output='screen'
        )
    ])