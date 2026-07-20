import rclpy
from rclpy.node import Node
from set_speed_manager.manager import SetSpeedManager

from std_msgs.msg import Int32
from std_srvs.srv import Trigger


class SetSpeedNode(Node):
    def __init__(self):
        super().__init__('set_speed')

        self.speed_setpoint = SetSpeedManager()
        self.vehicle_speed = 0

        self.publisher_ = self.create_publisher(
            Int32, 'speed_setpoint', 10
        )

        self.subscriber_ = self.create_subscription(
            Int32, 'vehicle_speed', self.vehicle_speed_callback, 10
        )

        self.increment_service_ = self.create_service(
            Trigger, 'increment', self.increment_callback
        )

        self.decrement_service_ = self.create_service(
            Trigger, 'decrement', self.decrement_callback
        )

        self.set_service_ = self.create_service(
            Trigger, 'set', self.set_callback
        )

        timer_period_s = 0.5
        self.timer_ = self.create_timer(timer_period_s, self.timer_callback)

        self.get_logger().info('Set speed node started!')

    def timer_callback(self):
        msg = Int32()
        msg.data = self.speed_setpoint.speed_mph
        self.publisher_.publish(msg)

    def vehicle_speed_callback(self, msg):
        self.vehicle_speed = msg.data

    def increment_callback(self, request, response):
        self.speed_setpoint.increment_speed()

        response.success = True
        response.message = 'Incrementing Speed!'

        self.get_logger().info(response.message)

        return response

    def decrement_callback(self, request, response):
        self.speed_setpoint.decrement_speed()

        response.success = True
        response.message = 'Decrementing Speed!'

        self.get_logger().info(response.message)

        return response

    def set_callback(self, request, response):
        self.speed_setpoint.set_speed(self.vehicle_speed)

        response.success = True
        response.message = f'Set speed to {self.vehicle_speed}!'

        self.get_logger().info(response.message)

        return response


def main(args=None):
    rclpy.init(args=args)
    node = SetSpeedNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
