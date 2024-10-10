# Copyright 2023-2024 Herman Ye@Auromix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

"""
AuroJoystickROSController is a ROS node that enables control of a robot using an Auro joystick.

This class initializes a ROS node, sets up a publisher to send velocity commands to the robot, and registers event handlers for joystick movements and button presses. It allows for controlling the robot's linear and angular velocities via joystick input and provides a service to reset the robot when a specific button is pressed.

Attributes:
    cmd_vel_pub (rospy.Publisher): Publisher for sending Twist messages to the robot.
    joystick (AuroJoystick): Instance of the AuroJoystick for handling joystick input.
    cmd (Twist): Twist message for controlling robot movement.
    reset_service (rospy.ServiceProxy): Service proxy for resetting the robot.

Methods:
    _init_joystick(): Registers joystick event handlers.
    on_left_stick_moved(x, y): Handles left joystick movement for linear control.
    on_right_stick_moved(x, y): Handles right joystick movement for angular control.
    on_button_b_pressed(): Calls the reset service when button B is pressed.
    run(): Starts the joystick and keeps the node running.
"""

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from auro_joystick import AuroJoystick

CMD_VEL_TOPIC = "/turtle1/cmd_vel"
RESET_SERVICE = "/reset"
MAX_LINEAR_VELOCITY = 2.0
MAX_ANGULAR_VELOCITY = 2.0
MAX_STICK_VALUE = 32767
MAX_TRIGGER_VALUE = 255


class AuroJoystickROSController:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node("auro_joystick_ros_controller", anonymous=True)

        # Create a publisher to send velocity commands to the robot
        self.cmd_vel_pub = rospy.Publisher(CMD_VEL_TOPIC, Twist, queue_size=10)

        # Initialize the joystick
        self.joystick = AuroJoystick()
        self._init_joystick()

        # Create a Twist message for controlling the robot
        self.cmd = Twist()
        # Initialize the reset service client
        rospy.wait_for_service(RESET_SERVICE)
        self.reset_service = rospy.ServiceProxy(RESET_SERVICE, Empty)

        rospy.loginfo(
            "Joystick controller initialized. Use the joystick to control the robot."
        )

    def _init_joystick(self):
        # Register event handlers for joystick movements and button presses
        self.joystick.register_event_handler(
            self.on_left_stick_moved, "left_stick_moved"
        )
        self.joystick.register_event_handler(
            self.on_right_stick_moved, "right_stick_moved"
        )
        self.joystick.register_event_handler(
            self.on_button_b_pressed, "button_b_pressed"
        )

    def on_left_stick_moved(self, x, y):
        # Control linear movement with the left joystick
        self.cmd.linear.x = x / MAX_STICK_VALUE * MAX_LINEAR_VELOCITY
        self.cmd.linear.y = y / MAX_STICK_VALUE * MAX_LINEAR_VELOCITY
        self.cmd_vel_pub.publish(self.cmd)

    def on_right_stick_moved(self, x, y):
        # Control angular rotation with the right joystick
        self.cmd.angular.z = y / MAX_STICK_VALUE * MAX_ANGULAR_VELOCITY
        self.cmd_vel_pub.publish(self.cmd)

    def on_button_b_pressed(self):
        # Call the reset service when button B is pressed
        try:
            self.reset_service()
            rospy.loginfo("Turtle has been reset!")
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)

    def run(self):
        # Main loop to keep the node running
        self.joystick.start()
        rospy.spin()


def main():
    controller = AuroJoystickROSController()
    controller.run()


if __name__ == "__main__":
    main()
