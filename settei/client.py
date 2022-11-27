import sys

from settei_interfaces.srv import ReadData
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(ReadData, 'Read')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = ReadData.Request()

    def send_request(self, package, robot, branch):
        self.req.package = package
        self.req.robot = robot
        self.req.branch = branch
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(sys.argv[1], sys.argv[2], sys.argv[3])
    minimal_client.get_logger().info(
        f''' {sys.argv[1]} ; {sys.argv[2]} ; {sys.argv[3]} :
            {response.filename_array} |
            {response.data_array}''')

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()