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

        timer_period_s = 0.5
        self.timer_ = self.create_timer(timer_period_s, self.timer_callback)

        self.get_logger().info('Set speed node started!')

    def timer_callback(self):
        msg = Int32()
        msg.data = self.speed_setpoint.speed_mph
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SetSpeedNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
