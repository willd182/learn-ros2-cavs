# Node Interface Testing
Now that your software module is wrapped in a node, the new interface must be tested. 

## Setup Actions
Build and source your workspace, then run your node.

```bash
ros2 run set_speed_manager set_speed_node
```

In a new terminal, publish data to the input topic of this node

```bash
ros2 topic pub /vehicle_speed std_msgs/msg/Int32 'data: 10'
```

> **Note:** Pressing `tab` in the terminal will sometimes autocomplete these lines.

## Service Testing
With the node running and data being published to the input topic, you can now test each service. After each check, use the following command to see the value of the output topic `/speed_setpoint`. 

```bash
ros2 topic echo /speed_setpoint --once
```

> **Note:** The "correct" values assume these services are called in order. Of course, you could call the services in another order and get different values.

### Set Functionality
First, start by calling the `/set` service.

```bash
ros2 service call /set std_srvs/srv/Trigger
```

Then check the value published to the `/speed_setpoint` topic, it should be `10`.

### Increment Functionality
Next, call the `/increment` service.

```bash
ros2 service call /increment std_srvs/srv/Trigger
```

Then check the value published to the `/speed_setpoint` topic, it should be `15`.
### Decrement Functionality
Finally, call the `/decrement` service.

```bash
ros2 service call /decrement std_srvs/srv/Trigger
```

Then check the value published to the `/speed_setpoint` topic, it should be `10`.

## Final Note and Pull Request
These checks verify that the ROS interface is correctly integrated with your software module. The module's requirements should already be validated through your unit tests, so less robust checks are needed here. Avoid implementing new functionality at the node level that escapes your unit tests.

From here, commit your latest changes and **open a pull request** on github. This will prompt a review of your code and any feedback. Congratulations!
