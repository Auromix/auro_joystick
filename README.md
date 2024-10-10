[![Official](https://img.shields.io/badge/Official%20-Auromix-blue?style=flat&logo=world&logoColor=white)](https://github.com/Auromix) &nbsp;
[![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-green)](https://ubuntu.com/) &nbsp;
[![LICENSE](https://img.shields.io/badge/license-Apache--2.0-informational)](https://github.com/Auromix/auro_joystick/blob/ros2-humble/LICENSE) &nbsp;
[![GitHub Repo stars](https://img.shields.io/github/stars/Auromix/auro_joystick?style=social)](https://github.com/Auromix/auro_joystick/stargazers) &nbsp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Hermanye233?style=social)](https://twitter.com/Hermanye233) &nbsp;

# 🎮 Auro Joystick

Auro Joystick is a Python library designed for interfacing with joystick devices in robotics applications, offering robust support for ROS to facilitate easy integration.

## 🚀 Features

- **Joystick Detection:** Automatically identifies supported joystick devices.
- **Event Handling:** Efficiently processes input events for joystick buttons and axes.
- **ROS Compatibility:** Seamlessly integrates with both ROS1 and ROS2 for robotic systems.
- **Configurable Logging:** Delivers comprehensive logging for straightforward debugging.
- **Custom Event Handlers:** Supports the registration of custom event handlers for specific joystick actions.

## 🧪 Testing Conditions

Auro Joystick has been tested on the `Beitong` gamepad.

It is also compatible with other controllers that follow the `Xbox` layout.

## ⚙️ Installation

To install Auro Joystick, you can use one of the following methods:

```bash
# Install from PyPI
pip install auro_joystick
```

```bash
# Install from the current directory (local development)
pip install .
```

## 🔥 Quickstart

You can find detailed examples for the project in the `examples` directory of the repository.

### Print Input

This example will display the current inputs and corresponding values from your gamepad:

```bash
python examples/print_input.py
```

### ROS Example

Use the `left joystick` to control the movement of a turtle in Turtlesim, while the `right joystick` will manage its rotation.

Press the `B` key to reset the turtle.

```bash
# [Terminal 1]
# Run roscore
roscore
```

```bash
# [Terminal 2]
# Run Turtlesim
rosrun turtlesim turtlesim_node
```

```bash
# [Terminal 3]
# Run the example
python examples/control_ros_turtlesim.py
```

## 🧑‍💻 Documentation

For comprehensive documentation, please refer to the comments within the source code and examples.

## 🙋 Troubleshooting

If you encounter any issues or have questions regarding this package, please contact the maintainers:

- Herman Ye @ Auromix (Email: <hermanye233@icloud.com>)

## 📜 License

```text
Copyright 2023-2024 Herman Ye@Auromix

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific
language governing permissions and limitations under the License.
```

## 🏆 Contributing

Contributions are welcome! Please follow the guidelines provided in the repository for contributing.
