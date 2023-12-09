# twist_controller
ROS 2 Package to efficiently send twist messages to the Twizy via the command line
### Requirements
- [SD-VehicleInterface](https://github.com/Monash-Connected-Autonomous-Vehicle/SD-VehicleInterface) should be in the same `~/<workspace>/src` directory as this package

### Running
- If SD-VehicleInterface or this package is already launched: run the `twist_controller` on a new terminal: 
	- `source install/setup.bash`  
	- `ros2 run twist_controller twist_controller`

- To launch `sd_vehicle_interface`, `foxglove_bridge` and/or this node: 
	- `ros2 launch twist_controller twist_controller.launch.py`
	

Following arguments when using `ros2 launch`:

| arg                | values                                    | default   | description                                |
| ------------------ | ----------------------------------------- | --------- | ------------------------------------------ |
| sd_speed_source    | {vehicle_can_speed, imu_speed, ndt_speed} | ndt_speed | Input vehicle speed                        |
| sd_simulation_mode | {true, false}                             | false      | Use on the car or on the Gazebo simulation |
| launch_foxglove    | {true, false}                             | true     | Launch foxglove bridge                     |
| twist_terminal     | {true, false}                             | false      | Create new terminal for twist controlling  |
| record     | {true, false}                             | false      | Record bag file of twist_cmd and sd_current_twist  |

- Arguments are entered using `<arg_description>`:=`<value>`. E.g. `ros2 launch twist_controller twist_controller.launch.py sd_simulation_mode:=true` 

- Note: if you're in a docker container, `twist_terminal`:=`true` will not work. You'll have to `ros2 run twist_controller twist_controller` in a new terminal
- If you're not using a docker container and there is an error in launching, ensure `gnome-terminal` is installed:
	- `sudo apt update`
	- `sudo apt -y install gnome-terminal libcanberra-gtk-module libcanberra-gtk3-module dbus-x11`
- If errors persist, resort to launching with default args and running this node in a new terminal