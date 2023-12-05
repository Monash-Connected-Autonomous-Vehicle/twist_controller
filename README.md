# twist_controller
ROS 2 Package to efficiently send twist messages to the Twizy via the command line
### Requirements
- [SD-VehicleInterface](https://github.com/Monash-Connected-Autonomous-Vehicle/SD-VehicleInterface) should be in the same `~/<workspace>/src` directory as this package

### Running
- To run the `twist_controller` on a new terminal: 
	- `source install/setup.bash`  
	- `ros2 run twist_controller twist_controller`

- To launch `sd_vehicle_interface`, `foxglove_bridge` and/or this node: 
	- `ros2 launch twist_controller twist_controller.launch.py`
	- If there is an error, ensure `gnome-terminal` is installed:
		- `sudo apt update`
		- `sudo apt -y install gnome-terminal libcanberra-gtk-module libcanberra-gtk3-module dbus-x11`

Following arguments when using `ros2 launch`:

| arg                | values                                    | default   | description                                |
| ------------------ | ----------------------------------------- | --------- | ------------------------------------------ |
| sd_speed_source    | {vehicle_can_speed, imu_speed, ndt_speed} | ndt_speed | Input vehicle speed                        |
| sd_simulation_mode | {true, false}                             | true      | Use on the car or on the Gazebo simulation |
| launch_foxglove    | {true, false}                             | false     | Launch foxglove bridge                     |
| twist_terminal     | {true, false}                             | true      | Create new terminal for twist controlling  |

- Arguments are enter in this format: `ros2 launch twist_controller twist_controller sd_simulation_mode:=false` 