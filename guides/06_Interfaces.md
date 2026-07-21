# Node Interfaces
The node you've created needs [interfaces](https://docs.ros.org/en/jazzy/Concepts/Basic/Interfaces-Topics-Services-Actions.html) to communicate. The three types of interfaces are [topics](https://docs.ros.org/en/jazzy/Concepts/Basic/About-Topics.html), [services](https://docs.ros.org/en/jazzy/Concepts/Basic/About-Services.html), and [actions](docs.ros.org/en/jazzy/Concepts/Basic/About-Actions.html).

## Adding a Topic
First, we'll add a topic to publish the current set speed at a fixed rate. This takes involves steps: **registering a publisher** and **adding a timer callback** to periodically publish the data.

To register a publisher, we need to define the message type, topic name, and [Quality of Service](https://medium.com/@mohamedaswer1706/understanding-qos-in-ros-2-ensuring-reliable-communication-b3500924eaff) (QoS). 

```python
import rclpy
from rclpy.node import Node
from set_speed_manager.manager import SetSpeedManager

from std_msgs.msg import Int32


class SetSpeedNode(Node):
    def __init__(self):
        super().__init__('set_speed')
        self.speed_setpoint = SetSpeedManager()

        self.publisher_ = self.create_publisher(
            Int32,
            'speed_setpoint',
            10
        )

        self.get_logger().info('Set speed node started!')
```

> **Note:** Passing `10` is shorthand for using the default QoS profile with a history depth of 10. For more advanced communication requirements, create and pass a custom `QoSProfile` instead.

At this point, the node has a publisher, but it never sends any messages. Next, we need to add a timer callback to publish data. Start by adding the following lines to the `__init__` function:

```python
timer_period_s = 0.5
self.timer_ = self.create_timer(timer_period_s, self.timer_callback)
```

Then, define the timer callback inside `SetSpeedNode`:

```python
def timer_callback(self):
    msg = Int32()
    msg.data = self.speed_setpoint.speed_mph
    self.publisher_.publish(msg)
```
Now, as your node runs, the `timer_callback` function will be called at a fixed rate and publish to the `/speed_setpoint` topic.

### Dependency Management
Since this node uses `std_msgs.msg.Int32`, add `std_msgs` as a dependency in your `package.xml`:
```xml
<depend>std_msgs</depend>
```

### Listening to a topic
Rebuild and run your node using the instructions at the end of [Node Creation](./05_NodeCreation.md). Keep this running and in a new terminal run:

```bash
ros2 topic echo /speed_setpoint
```

You should see the published messages from your node printed to the console.

## Adding a Service
Services are useful for **request-response** interactions such as changing the set speed. In this example, we'll use the standard [Trigger](https://docs.ros.org/en/jazzy/p/std_srvs/srv/Trigger.html) service to increment the speed when requested.

To register a service, we need to define the service type, service name, and callback function.

```python
import rclpy
from rclpy.node import Node
from set_speed_manager.manager import SetSpeedManager

from std_srvs.srv import Trigger

class SetSpeedNode(Node):
    def __init__(self):
        super().__init__('set_speed')
        self.speed_setpoint = SetSpeedManager()

        self.increment_service_ = self.create_service(
            Trigger,
            'increment',
            self.increment_callback
        )

        self.get_logger().info('Set speed node started!')
```

Next, define the service callback inside `SetSpeedNode`:

```python
def increment_callback(self, request, response):
    self.speed_setpoint.increment_speed()
    
    response.success = True
    response.message = 'Incrementing Speed!'

    self.get_logger().info(response.message)
    
    return response
```

> **Note:** A more robust implementation could set success based on whether the speed actually increased or was limited.

### Dependency Management
Since this node uses `std_srvs.srv.Trigger`, add `std_srvs` as a dependency in your `package.xml`:
```xml
<depend>std_srvs</depend>
```

### Calling a Service
Follow the earlier instructions about *listening to a topic* and then in a new terminal call:

```bash
ros2 service call /increment std_srvs/srv/Trigger
```

From the above you command, you'll see a response like:

> waiting for service to become available...  
> requester: making request: std_srvs.srv.Trigger_Request()  
> 
> response:  
> std_srvs.srv.Trigger_Response(success=True, message='Incrementing Speed!') 

If you're listening to the `/speed_setpoint` topic, you should also see the set speed increase.

# Interface Blueprint
For your `SetSpeedNode`, below are the recommended interfaces:

| Interface Name    | Type      | Description |
|-------------------|-----------|-------------|
| `/speed_setpoint` | Publish   | Publishes the set speed for other nodes|
| `/vehicle_speed`  | Subscribe | Subscribes to current vehicle speed |
| `/increment`      | Service   | Increments the set speed by 5 mph |
| `/decrement`      | Service   | Decrements the set speed by 5 mph |
| `/set`            | Service   | Changes the set speed to the current vehicle speed |

> Note: Use this [tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html) for adding a subscription