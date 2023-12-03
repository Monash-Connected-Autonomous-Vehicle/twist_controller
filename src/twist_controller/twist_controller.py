#!/usr/bin/env python3
import rclpy
from geometry_msgs.msg import Twist
class TwistController:
    def __init__(self):
        self.twist_pub = self.create_publisher(Twist, '/twist', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
    def timer_callback(self):
        linear_x = float(input("Enter linear x value: "))
        angular_z = float(input("Enter angular z value: "))
        twist_msg = Twist()
        twist_msg.linear.x = linear_x
        twist_msg.angular.z = angular_z
        self.twist_pub.publish(twist_msg)
def main(args=None):
    rclpy.init(args=args)
    controller = TwistController()
    rclpy.spin(controller)
    rclpy.shutdown()
if __name__ == '__main__':
    main()