import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class VehicleSpeedNode(Node):
    def __init__(self):
        super().__init__('vehicle_speed')

        self.declare_parameter('speed', 0)

        self.publisher_ = self.create_publisher(
            Int32, 'vehicle_speed', 10
        )

        timer_period = 0.5
        self.timer_ = self.create_timer(
            timer_period, self.timer_callback
        )

    def timer_callback(self):
        msg = Int32()
        msg.data = self.get_parameter('speed').value
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = VehicleSpeedNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
