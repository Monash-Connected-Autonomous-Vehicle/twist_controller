import rclpy
from autoware_auto_control_msgs.msg import AckermannControlCommand
from builtin_interfaces.msg import Time


def main():
    DEG_TO_RAD = 0.01745329252
    rclpy.init()
    node = rclpy.create_node('ackermann_controller_node')
    Ackermann = AckermannControlCommand
    pub = node.create_publisher(Ackermann, 'ackermann_cmd', 10)

    ack_msg = Ackermann()

    print("Enter speed and angle values to publish to /ackermann_cmd topic.")
    print("Press Enter (without a number) to use last re-publish last ackermann command.")
    print("Press Ctrl+C to stop the program.\n")

    last_speed = 0
    last_angle = 0

    while True:
        speed = input("Enter speed (m/s) value: ")
        angle = input("Enter tire angle (degrees, positive = left steer): ")

        if speed == "":
            speed = last_speed

        if angle == "":
            angle = last_angle

        try:
            speed = float(speed)
            angle = float(angle)
            ack_msg.longitudinal.speed = speed
            ack_msg.lateral.steering_tire_angle = angle * DEG_TO_RAD
            
            timestamp = Time()
            timestamp.sec, timestamp.nanosec = rclpy.clock.Clock().now().seconds_nanoseconds()
            ack_msg.stamp = timestamp
            
            pub.publish(ack_msg, )
            print(f"Published values: speed = {speed}, angle = {angle}\n")

            last_speed = speed
            last_angle = angle
            
        except ValueError:
            print("Invalid input. Please enter numeric values for speed and angle.")


if __name__ == '__main__':
    main()
