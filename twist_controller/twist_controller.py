import rclpy
import geometry_msgs.msg

def main():
    rclpy.init()
    node = rclpy.create_node('twist_controller_node')
    TwistMsg = geometry_msgs.msg.TwistStamped
    pub = node.create_publisher(TwistMsg, 'twist_cmd', 10)

    twist_msg = TwistMsg()

    twist = twist_msg.twist
    twist_msg.header.stamp = node.get_clock().now().to_msg()

    print("Enter twist.linear.x and twist.angular.z values to publish to /twist_cmd topic.")
    print("Press Enter (without a number) to use last re-publish last twist value.")
    print("Press Ctrl+C to stop the program.\n")

    last_linear_x = 0
    last_angular_z = 0

    while True:
        # Print d
        linear_x = input("Enter twist.linear.x value: ")
        angular_z = input("Enter twist.angular.z value: ")

        if linear_x == "":
            linear_x = last_linear_x

        if angular_z == "":
            angular_z = last_angular_z

        try:
            linear_x = float(linear_x)
            angular_z = float(angular_z)
            twist_msg.header.stamp = node.get_clock().now().to_msg()
            twist.linear.x = linear_x
            twist.angular.z = angular_z
            
            pub.publish(twist_msg, )
            print(f"Published values: twist.linear.x = {linear_x}, twist.angular.z = {angular_z}\n")

            last_linear_x = linear_x
            last_angular_z = angular_z
            
        except ValueError:
            print("Invalid input. Please enter numeric values for twist.linear.x and twist.angular.z.")


if __name__ == '__main__':
    main()
