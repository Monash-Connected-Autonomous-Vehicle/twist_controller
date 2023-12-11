import os
from launch.actions import ExecuteProcess
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'twist_terminal',
            default_value='false',
            description='Launch twist terminal',
        ),

        Node(
            package='twist_controller',
            executable='twist_controller',
            name='twist_controller_node',
            output='screen',
            prefix='gnome-terminal --',
            condition=IfCondition(LaunchConfiguration('twist_terminal'))
        ),

        DeclareLaunchArgument(
            'sd_simulation_mode',
            default_value='false',
            description='Use on car on on simulation',
        ),

        DeclareLaunchArgument(
            'sd_speed_source',
            default_value='vehicle_can_speed',
            description='Input Vehicle Speed',
        ),

        IncludeLaunchDescription(
            XMLLaunchDescriptionSource(os.path.join(
                get_package_share_directory('sd_vehicle_interface'),
                'launch/sd_vehicle_interface.launch.xml'
            )),
            launch_arguments={
                'sd_simulation_mode': LaunchConfiguration('sd_simulation_mode'),
                'sd_speed_source': LaunchConfiguration('sd_speed_source'),
            }.items(),
        ),

        DeclareLaunchArgument(
            'launch_foxglove',
            default_value='true',
            description='Launch foxglove bridge',
        ),

        DeclareLaunchArgument(
            'port',
            default_value='8765',
            description='Port for the foxglove_bridge',
        ),

        IncludeLaunchDescription(
            XMLLaunchDescriptionSource(os.path.join(
                get_package_share_directory('foxglove_bridge'),
                'launch/foxglove_bridge_launch.xml'
            )),
            launch_arguments={'port': LaunchConfiguration('port')}.items(),
            condition=IfCondition(LaunchConfiguration('launch_foxglove'))
        ),

        DeclareLaunchArgument(
            'record',
            default_value='false',
            description='Record bag file of twist_cmd and sd_current_twist',
        ),

        ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '/twist_cmd', '/sd_current_twist'],
            output='screen',
            condition=IfCondition(LaunchConfiguration('record'))
        )
    ])
