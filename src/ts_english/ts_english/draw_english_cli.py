import sys
from custom_interfaces.srv import DrawEnglish
import rclpy
from rclpy.node import Node

class DrawEnglishCli(Node):
    
    def __init__(self):
        super().__init__('draw_english_client_node')
        self.cli = self.create_client(
            DrawEnglish, 'draw_english_service'
        )

        while not self.cli.wait_for_service(timeout_sec= 1.0):
            self.get_logger().info('Server not available...')
        
        self.req = DrawEnglish.Request()
    
    def send_request(self, line):
        self.req.line = line
        
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)

        return self.future.result()
    
def main(args = None):
    rclpy.init(args = args)

    draw_english_cli = DrawEnglishCli()

    line = str(sys.argv[1])
    response = draw_english_cli.send_request(line)
    draw_english_cli.get_logger().info('Drawing Done!')

    draw_english_cli.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__' :
    main()