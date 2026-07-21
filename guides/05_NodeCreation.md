# ROS2 Node Creation
To run your module inside the ROS2 environment, we'll put it inside a node. To start, create a new file called `set_speed_node.py` next to your software module.

## Creating a Node
A simple node can be created by inheriting from the `rclpy.node.Node` class:

```python
import rclpy
from rclpy.node import Node
from set_speed_manager.manager import SetSpeedManager

class SetSpeedNode(Node):
    def __init__(self):
        super().__init__('set_speed')
        self.speed_setpoint = SetSpeedManager()
        self.get_logger().info('Set speed node started!')
```

Then, in the same file, you'll need to write some code to create and spin up your node. 

```python
def main(args=None):
    rclpy.init(args=args)
    node = SetSpeedNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
Finally, add an entry point to `setup.py` by updating the following:
```python
entry_points={
    'console_scripts': [
        'set_speed_node = set_speed_manager.node:main'
    ],
},
```

## Running the Node
To run your node, first you need to build and source your package.

```bash
colcon build
source install/setup.bash
```

Then, you can run your node using the following command:

```bash
ros2 run set_speed_manager set_speed_node
```

The command will be blocking until you press `ctrl+c` in the terminal. You should also see the logger message:
> [INFO] [1784248910.278238748] [set_speed]: Set speed node started!