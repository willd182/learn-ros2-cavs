import rclpy
from rclpy.node import Node
from set_speed_manager.manager import SetSpeedManager


class SetSpeedNode(Node):
    def __init__(self):
        super().__init__('set_speed')
        self.speed_setpoint = SetSpeedManager()
        self.get_logger().info('Set speed node started!')


def main(args=None):
    rclpy.init(args=args)
    node = SetSpeedNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
