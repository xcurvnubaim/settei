from settei_interfaces.srv import GetData     # CHANGE

import rclpy
from rclpy.node import Node

from settei2 import read_data

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(GetData, 'get_data', self.get_data_callback)        # CHANGE

    def get_data_callback(self, request, response):
        response.filename_array,response.data_array = read_data(
            request.package,request.robot,request.branch
        )                                          # CHANGE
        self.get_logger().info(f'{response.filename_array} ; {response.data_array}') # CHANGE

        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()