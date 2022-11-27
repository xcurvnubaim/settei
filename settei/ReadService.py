from settei_interfaces.srv import ReadData
# from read import getdata
import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(ReadData, 'read_data', self.read_data)

    def read_data(self, request, response):
        # x = read(request.package,request.robot,request.branch)
        response.filename_array = 'hello world'
        # response.data_array = 'hello world'
        # self.get_logger().info('Incoming request\n: %s : %s : %s' % (request.package, request.robot,request.branch))

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()