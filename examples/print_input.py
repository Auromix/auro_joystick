"""
This module demonstrates how to use the AuroJoystick class to handle joystick events in a robotics context.

MyTestClass initializes an AuroJoystick instance and registers multiple event handlers for various joystick buttons and stick movements. The handlers print messages to the console when buttons are pressed or released and when the sticks are moved.

Users can replicate this example by:
1. Creating their own class that initializes an AuroJoystick instance.
2. Registering desired event handlers for the buttons and sticks they want to monitor.
3. Implementing their own logic within the handler methods.
4. Starting the joystick listening loop to receive input.

To run the example, ensure the AuroJoystick library is installed and properly set up for your joystick device.
"""

from auro_joystick import AuroJoystick


class MyTestClass:
    def __init__(self):
        self._init_joystick()
        print("MyTestClass initialized")

    def _init_joystick(self):
        # Initialize the auro joystick
        self.joystick = AuroJoystick()
        # Register event handlers you want to use
        self.joystick.register_event_handler(
            self.on_button_left_stick_pressed, "button_left_stick_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_left_stick_released, "button_left_stick_released"
        )
        self.joystick.register_event_handler(
            self.on_button_right_stick_pressed, "button_right_stick_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_right_stick_released, "button_right_stick_released"
        )
        self.joystick.register_event_handler(
            self.on_button_left_bumper_pressed, "button_left_bumper_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_left_bumper_released, "button_left_bumper_released"
        )
        self.joystick.register_event_handler(
            self.on_button_right_bumper_pressed, "button_right_bumper_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_right_bumper_released, "button_right_bumper_released"
        )
        self.joystick.register_event_handler(
            self.on_button_start_pressed, "button_start_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_start_released, "button_start_released"
        )
        self.joystick.register_event_handler(
            self.on_button_back_pressed, "button_back_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_back_released, "button_back_released"
        )
        self.joystick.register_event_handler(
            self.on_button_a_pressed, "button_a_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_a_released, "button_a_released"
        )
        self.joystick.register_event_handler(
            self.on_button_b_pressed, "button_b_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_b_released, "button_b_released"
        )
        self.joystick.register_event_handler(
            self.on_button_x_pressed, "button_x_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_x_released, "button_x_released"
        )
        self.joystick.register_event_handler(
            self.on_button_y_pressed, "button_y_pressed"
        )
        self.joystick.register_event_handler(
            self.on_button_y_released, "button_y_released"
        )
        self.joystick.register_event_handler(self.on_dpad_up_pressed, "dpad_up_pressed")
        self.joystick.register_event_handler(
            self.on_dpad_up_released, "dpad_up_released"
        )
        self.joystick.register_event_handler(
            self.on_dpad_down_pressed, "dpad_down_pressed"
        )
        self.joystick.register_event_handler(
            self.on_dpad_down_released, "dpad_down_released"
        )
        self.joystick.register_event_handler(
            self.on_dpad_left_pressed, "dpad_left_pressed"
        )
        self.joystick.register_event_handler(
            self.on_dpad_left_released, "dpad_left_released"
        )
        self.joystick.register_event_handler(
            self.on_dpad_right_pressed, "dpad_right_pressed"
        )
        self.joystick.register_event_handler(
            self.on_dpad_right_released, "dpad_right_released"
        )
        self.joystick.register_event_handler(
            self.on_left_trigger_pressed, "left_trigger_pressed"
        )
        self.joystick.register_event_handler(
            self.on_left_trigger_released, "left_trigger_released"
        )
        self.joystick.register_event_handler(
            self.on_right_trigger_pressed, "right_trigger_pressed"
        )
        self.joystick.register_event_handler(
            self.on_right_trigger_released, "right_trigger_released"
        )
        self.joystick.register_event_handler(
            self.on_left_stick_moved, "left_stick_moved"
        )
        self.joystick.register_event_handler(
            self.on_right_stick_moved, "right_stick_moved"
        )

    def my_button_a_function(self):
        print("Button A pressed")

    def on_button_left_bumper_pressed(self):
        print("Left bumper was pressed!")

    def on_button_left_bumper_released(self):
        print("Left bumper was released!")

    def on_button_right_bumper_pressed(self):
        print("Right bumper was pressed!")

    def on_button_right_bumper_released(self):
        print("Right bumper was released!")

    def on_button_left_stick_pressed(self):
        print("Left stick was pressed!")

    def on_button_left_stick_released(self):
        print("Left stick was released!")

    def on_button_right_stick_pressed(self):
        print("Right stick was pressed!")

    def on_button_right_stick_released(self):
        print("Right stick was released!")

    def on_button_start_pressed(self):
        print("Button Start was pressed!")

    def on_button_start_released(self):
        print("Button Start was released!")

    def on_button_back_pressed(self):
        print("Button Back was pressed!")

    def on_button_back_released(self):
        print("Button Back was released!")

    def on_button_a_pressed(self):
        print("Button A was pressed!")

    def on_button_a_released(self):
        print("Button A was released!")

    def on_button_b_pressed(self):
        print("Button B was pressed!")

    def on_button_b_released(self):
        print("Button B was released!")

    def on_button_x_pressed(self):
        print("Button X was pressed!")

    def on_button_x_released(self):
        print("Button X was released!")

    def on_button_y_pressed(self):
        print("Button Y was pressed!")

    def on_button_y_released(self):
        print("Button Y was released!")

    def on_dpad_up_pressed(self):
        print("DPad up was pressed!")

    def on_dpad_up_released(self):
        print("DPad up was released!")

    def on_dpad_down_pressed(self):
        print("DPad down was pressed!")

    def on_dpad_down_released(self):
        print("DPad down was released!")

    def on_dpad_left_pressed(self):
        print("DPad left was pressed!")

    def on_dpad_left_released(self):
        print("DPad left was released!")

    def on_dpad_right_pressed(self):
        print("DPad right was pressed!")

    def on_dpad_right_released(self):
        print("DPad right was released!")

    def on_left_trigger_pressed(self, value):
        print(f"Left trigger was pressed! Value:{value}")

    def on_left_trigger_released(self, value):
        print(f"Left trigger was released! Value:{value}")

    def on_right_trigger_pressed(self, value):
        print(f"Right trigger was pressed! Value:{value}")

    def on_right_trigger_released(self, value):
        print(f"Right trigger was released! Value:{value}")

    def on_left_stick_moved(self, x, y):
        print(f"Left stick was moved! X:{x} Y:{y}")

    def on_right_stick_moved(self, x, y):
        print(f"Right stick was moved! X:{x} Y:{y}")


def main():
    my_test_class = MyTestClass()
    # Start the joystick listening loop
    my_test_class.joystick.loop()


if __name__ == "__main__":
    main()
