# Vehicle Speed Node

The `SetSpeedNode` subscribes to `/vehicle_speed`, but there is currently no node publishing data on that topic. To fully test it, use the instructions in the [interfaces guide](./06_Interfaces.md) to create a second node called `VehicleSpeedNode` that publishes messages to `/vehicle_speed`.

> **Note:** For now just publish a constant vehicle speed of 0 mph.

The package will now contain:

```
set_speed_manager/
├── set_speed_manager/
|   ├── __init__.py
│   ├── set_speed_node.py
│   ├── vehicle_speed_node.py
│   └── manager.py
├── config/
├── launch/
└── package.xml
```

## Adding Parameters
In ROS2, [parameters](https://docs.ros.org/en/jazzy/Concepts/Basic/About-Parameters.html) can be defined to allow nodes to be configured without modifying source code. In this case, the vehicle speed is a good candidate for a parameterized value.

To declare a parameter, define its name and default value. Do this by adding the following to the `__init__` method:

```python
self.declare_parameter('speed', 0)
```

> **Note:** The data type of the parameter is inferred from the default value provided.

## Reading Parameters

A parameter can be retrieved using the `get_parameter` method, which returns an `Parameter` object. The parameter's value can then be accessed through its value attribute.

```python
def timer_callback(self):
    msg = Int32()
    msg.data = self.get_parameter('speed').value
    self.publisher_.publish(msg)
```

The node now publishes the configured speed instead of a hardcoded value.

## Command Line Parameter Configuration

Parameters can be changed when starting the node:

```bash
ros2 run set_speed_manager vehicle_speed_node \
  --ros-args \
  -p speed:=50
```

This runs the same node with:

- An initial speed of `50` mph.

No source code changes are required.

## Live Parameter Interactions

While the node is running, open a new terminal and list the available parameters:

```bash
ros2 param list
```

This should produce output similar to:

```text
/vehicle_speed:
  speed
  start_type_description_service
  use_sim_time
```

You can inspect the current value of the `speed` parameter with:

```bash
ros2 param get /vehicle_speed speed
```

Example output:

```text
Integer value is: 50
```

To change the parameter while the node is still running, use:

```bash
ros2 param set /vehicle_speed speed 75
```

Expected output:

```text
Set parameter successful
```
The new value is applied immediately without restarting the node. This allows parameters to be tuned at runtime, making it easy to adjust behavior while the system is operating.