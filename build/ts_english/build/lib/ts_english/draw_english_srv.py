import rclpy
from rclpy.node import Node

import time
import numpy as np

from geometry_msgs.msg import Twist
from custom_interfaces.srv import DrawEnglish
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import SetPen

class DrawEnglishSrv(Node):
    
    def __init__(self):
        super().__init__('draw_english_service_node')
        self.srv = self.create_service(
            DrawEnglish, 'draw_english_service', self.draw_english_callback
        )
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel',10)

        self.go = Twist()
        self.go.linear.x = 1.0
        self.go.angular.z = 0.0

        self.turn = Twist()
        self.turn.linear.x = 0.0
        self.turn.angular.z = 1.57079

        self.stop = Twist()
        self.stop.linear.x = 0.0
        self.stop.angular.z = 0.0

        self.line_req = SetPen.Request()

        self.start_time = self.get_clock().now().to_msg().sec
        self.clock_now = self.start_time

    def draw_english_callback(self, request, response):
        line = request.line
        
        self.get_logger().info('Received Request : draw %s' % request.line)
        
        self.turtle_draw(line)
        response.success = True

        return response
    
    def turtle_draw(self, line):
        line = [x.upper() for x in line]

        self.line_off()
        self.init_pose()

        self.get_logger().info('Turtle Starts Drawing...')
        for ch in line:
            self.draw_ch(ch)

    def init_pose(self):
        self.get_logger().info('Initializing Position...')

        init_pose_req = TeleportAbsolute.Request()
        init_pose_req.x = 0.1
        init_pose_req.y = 0.1
        init_pose_req.theta = 0.0

        self.init_future = self.create_client(
            TeleportAbsolute, '/turtle1/teleport_absolute'
        ).call_async(init_pose_req)

    def line_off(self):
        self.get_logger().info('Turning Line Off...')
        self.line_req.off = 1

        self.line_future = self.create_client(
            SetPen, '/turtle1/set_pen'
        ).call_async(self.line_req)

    def line_on(self):
        self.line_req.width = 3
        self.line_req.off = 0

        self.line_future = self.create_client(
            SetPen, '/turtle1/set_pen'
        ).call_async(self.line_req)

    def draw_ch(self, ch):
        if ch == 'A': 
            self.get_logger().info('drawing "A"...')

            self.draw_straight(3,1,0)
            self.draw_straight(2,8,1)
            self.draw_straight(2,-8,1)
            self.draw_straight(-3,4,0)
            self.draw_straight(2,0,1)
            self.draw_straight(3,-5,0)

        elif ch == 'b': self.draw_b()
        elif ch == 'c': self.draw_c()
        elif ch == 'd': self.draw_d()
        elif ch == 'e': self.draw_e()
        elif ch == 'f': self.draw_f()
        elif ch == 'g': self.draw_g()
        elif ch == 'h': self.draw_h()
        elif ch == 'i': self.draw_i()
        elif ch == 'j': self.draw_j()
        elif ch == 'k': self.draw_k()
        elif ch == 'l': self.draw_l()
        elif ch == 'm': self.draw_m()
        elif ch == 'n': self.draw_n()
        elif ch == 'o': self.draw_o()
        elif ch == 'p': self.draw_p()
        elif ch == 'q': self.draw_q()
        elif ch == 'r': self.draw_r()
        elif ch == 's': self.draw_s()
        elif ch == 't': self.draw_t()
        elif ch == 'u': self.draw_u()
        elif ch == 'v': self.draw_v()
        elif ch == 'w': self.draw_w()
        elif ch == 'x': self.draw_x()
        elif ch == 'y': self.draw_y()
        elif ch == 'z': self.draw_z()

    def draw_straight(self, x_coor, y_coor, draw_on):
        self.get_logger().info('Drawing Straight : (%s %s %d)' % (x_coor, y_coor, draw_on))

        if draw_on:
            self.line_on()
        else:
            self.line_off()

        self.turn_angle = np.arctan2(y_coor , x_coor)
        if self.turn_angle < 0 :
            self.turn_angle += 3.14159 * 2

        self.go_dist = np.sqrt(x_coor * x_coor + y_coor * y_coor)

        self.get_logger().info('%f %f' %(self.turn_angle, self.go_dist))

        self.timestamp()
        while (self.clock_now - self.start_time) < (self.turn_angle / 1.57079):
            self.publisher_.publish(self.turn)
            self.clock_now = self.get_clock().now().to_msg().sec        
        self.publisher_.publish(self.stop)
        
        self.timestamp()
        while (self.clock_now - self.start_time) < (self.go_dist):
            self.publisher_.publish(self.go)
            self.clock_now = self.get_clock().now().to_msg().sec        
        self.publisher_.publish(self.stop)
        
        self.timestamp()
        while (self.clock_now - self.start_time) < (4 - (self.turn_angle / 1.57079)):
            self.publisher_.publish(self.turn)
            self.clock_now = self.get_clock().now().to_msg().sec        
        self.publisher_.publish(self.stop)
    
    def timestamp(self):
        self.start_time = self.get_clock().now().to_msg().sec
        self.clock_now = self.start_time
    

def main(args = None):
    rclpy.init(args = args)

    draw_english_srv = DrawEnglishSrv()

    rclpy.spin(draw_english_srv)

    draw_english_srv.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__' :
    main()