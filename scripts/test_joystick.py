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

import evdev
from evdev import ecodes

# List all input devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

# Search for the first gamepad device
gamepad = None
for device in devices:
    if (
        "pad" in device.name.lower()
    ):  # Identify gamepad by checking if 'pad' is in the device name
        gamepad = device
        print(f"Found gamepad: {device.name} at {device.path}")
        break

if gamepad is None:
    print("No gamepad found.")
else:
    print("Gamepad connected, listening for events...")

    # Read events from the gamepad
    for event in gamepad.read_loop():

        if event.type == ecodes.EV_KEY:
            # Capture key events like ABXY, D-pad, shoulder buttons, etc.
            key_event = evdev.categorize(event)
            print(
                f"Button event: Keycode: {key_event.keycode}, State: {key_event.keystate}, Code: {event.code}"
            )

        elif event.type == ecodes.EV_ABS:
            # Capture axis events like joystick, trigger, etc.
            absevent = evdev.categorize(event)
            if event.code == ecodes.ABS_X or event.code == ecodes.ABS_Y:
                # Joystick event (X or Y axis)
                print(
                    f"Left Stick: Code: {absevent.event.code}, Value: {absevent.event.value}"
                )
            elif event.code == ecodes.ABS_RX or event.code == ecodes.ABS_RY:
                # Right joystick event
                print(
                    f"Right Stick: Code: {absevent.event.code}, Value: {absevent.event.value}"
                )
            elif event.code == ecodes.ABS_Z or event.code == ecodes.ABS_RZ:
                # Trigger event
                print(
                    f"Trigger: Code: {absevent.event.code}, Value: {absevent.event.value}"
                )
            else:
                print(
                    f"Other ABS event: KeyCode: {absevent.event.code} Code: {absevent.event.code}, Value: {absevent.event.value}"
                )

        elif event.type == ecodes.EV_SYN:
            # Sync event, marks the end of a set of events
            pass
