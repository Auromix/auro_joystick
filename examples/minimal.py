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

import time
from auro_joystick import AuroJoystick


# Your callback function
def on_button_a_pressed():
    print("Button A pressed!")


# Init the joystick
joystick = AuroJoystick()
# Register the function for button A
joystick.register_event_handler(on_button_a_pressed, "button_a_pressed")

# Start the joystick
joystick.start()

# Your loop
while True:
    time.sleep(0.05)
