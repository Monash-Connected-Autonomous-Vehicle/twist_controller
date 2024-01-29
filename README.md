# twist_controller
ROS 2 Package to efficiently send twist messages to the Twizy via the command line
### Requirements
- [SD-VehicleInterface](https://github.com/Monash-Connected-Autonomous-Vehicle/SD-VehicleInterface) should be in the same `~/<workspace>/src` directory as this package


### Set up for Testing SD-VehicleInterface with Twist Controller

After creating a ROS2 workspace, clone [twist_controller](https://github.com/Monash-Connected-Autonomous-Vehicle/twist_controller) & [SD-VehicleInterface](https://github.com/Monash-Connected-Autonomous-Vehicle/SD-VehicleInterface/tree/main) into `src`

If you want to test Autoware msgs, ensure you clone the correct Ackermann branches and do the following:
Clone [Autoware Auto Msgs](https://github.com/tier4/autoware_auto_msgs) `src`
Install correct version of setuptools
```python
pip install setuptools==58.2.0
```

Install foxglove bridge and can_msgs:
```bash
source /opt/ros/humble/setup.bash
sudo apt-get install ros-humble-can-msgs
sudo apt install ros-$ROS_DISTRO-foxglove-bridge
```


### Using SD-VehicleInterface with Twist Controller
- View bugs section if you encounter any errors (end of README)
- Follow [these steps](https://www.notion.so/monashcav/Hardware-in-the-Loop-Demo-4eb8536a21734a2da9ecee6120d6be9f?pvs=4#5bb39aa187f34f40bfd06b62536a3b0c) up to step 5. (Steps 4-5 are often already done)
- ssh to the SD Alienware and go to the SD-VehicleInterface directory
```
cd /home/mcav/test_ack_ws
```

Terminal 1:
- Ensure PEAK CAN is connected, light should be blinking red after running the following command: 
```
sudo modprobe peak_usb
sudo ip link set down can0 && sudo ip link set can0 up type can bitrate 500000
```
- Launch SD-VehicleInterface:
```
source install/setup.bash
ros2 run twist_controller twist_controller
```
- After launching, you should see the following: The red light in the car should stop blinking. At this time you turn the knob clockwise to turn on Autonomous Mode.
- Note: Output of `cpp` files will be found in this terminal

Terminal 2:
- Run Twist controller:
```
source install/setup.bash
ros2 run twist_controller twist_controller
```

### Twist Controller Arguments

Following arguments when using `ros2 launch`:

| arg                | values                                    | default   | description                                |
| ------------------ | ----------------------------------------- | --------- | ------------------------------------------ |
| sd_speed_source    | {vehicle_can_speed, imu_speed, ndt_speed} | vehicle_can_speed | Input vehicle speed                        |
| sd_simulation_mode | {true, false}                             | false      | Use on the car or on the Gazebo simulation |
| launch_foxglove    | {true, false}                             | true     | Launch foxglove bridge                     |
| twist_terminal     | {true, false}                             | false      | Create new terminal for twist controlling  |
| record     | {true, false}                             | false      | Record bag file of twist_cmd and sd_current_twist  |

- Arguments are entered using `<arg_description>`:=`<value>`. E.g. `ros2 launch twist_controller twist_controller.launch.py sd_simulation_mode:=true` 


### Common Bugs
#### `can0` - No buffer space available
If still launching with errors, it's usually because there are other ros topics already existing: There should only be `/rosout` and `/parameter_events` before launching.
If that's the case: restart the docker container and/or laptop and try again.


#### `twist_cmd` not shown on foxglove
- This error seems to go away whenever the twist_controller node is launch before or at the same time as the launch file


#### Launch file not automatically launching new terminal
- Note: if you're in a docker container, `twist_terminal`:=`true` will not work. You'll have to `ros2 run twist_controller twist_controller` in a new terminal
- If you're not using a docker container and there is an error in launching, ensure `gnome-terminal` is installed:
	- `sudo apt update`
	- `sudo apt -y install gnome-terminal libcanberra-gtk-module libcanberra-gtk3-module dbus-x11`
- If errors persist, resort to launching with default args and running this node in a new terminal