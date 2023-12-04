from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='twist_controller',
            executable='twist_controller',
            name='twist_controller_node',
            output='screen',
            prefix = 'gnome-terminal --',
        ),

        DeclareLaunchArgument(
            'sd_simulation_mode',
            default_value='true',
            description='Description of sd_simulation_mode argument',
        ),
        
        DeclareLaunchArgument(
            'sd_speed_source',
            default_value='ndt_speed',
            description='Description of sd_speed_source argument',
        ),

        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([
        #         get_package_share_directory('sd_vehicle_interface'), '/launch/sd_vehicle_interface.launch.py'
        #     ]),
        #     launch_arguments={
        #         'sd_simulation_mode': LaunchConfiguration('sd_simulation_mode'),
        #         'sd_speed_source': LaunchConfiguration('sd_speed_source'),
        #     }.items(),
        # ),

    ])