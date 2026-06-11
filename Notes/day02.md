# Day 2

## Concepts Learned

- Workspace
- Package
- Node
- Timer
- Publisher

## Commands Used

source /opt/ros/jazzy/setup.bash

mkdir -p ~/ros2_ws/src

ros2 pkg create --build-type ament_python my_first_robot

colcon build

source install/setup.bash

ros2 run my_first_robot first_node

ros2 topic list

ros2 topic echo /my_topic

## Package Structure

my_first_robot
│
├── package.xml
├── setup.py
└── my_first_robot
      ├── __init__.py
      └── my_first_node.py

## Understanding

Node
↓
Timer
↓
Create Message
↓
Publish Message
↓
Topic
↓
Subscriber
