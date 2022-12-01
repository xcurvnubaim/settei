import rclpy
from rclpy.node import Node
from settei import write_data
from settei_interfaces.msg import WriteData        


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            WriteData,                                              
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        write_data(msg.package, msg.robot, msg.branch,
        msg.filename_array,msg.data_array)

        self.get_logger().info(f'''
        {msg.package} ; {msg.robot} ; {msg.branch} ;
        {msg.filename_array} ; {msg.data_array}
        ''') 


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()