import rclpy
from rclpy.node import Node

from settei_interfaces.msg import WriteData    # CHANGE


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(WriteData, 'topic', 10)     # CHANGE
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = WriteData()                                           # CHANGE
        msg.package = "aruku"
        msg.robot = "robot"
        msg.branch = "master"
        msg.filename = "config.json"
        msg.data = "hello world"                                # CHANGE
        self.publisher_.publish(msg)
        # self.get_logger().info('Publishing: "%d"' % msg.num)  # CHANGE
        # self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()