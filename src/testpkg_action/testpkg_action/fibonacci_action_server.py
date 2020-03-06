import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
# from testpkg_action.action import Fibonacci
# from testpkg_action import *
# from testpkg_action import Fibonacci
# from testpkg_action.action import *
# from action import *
# from testpkg_action.action import *

import sys
# sys.path.append('/home/rajendra/ros2eloquent_catkin_ws/src/testpkg_action/action')
sys.path.append('/home/rajendra/ros2eloquent_catkin_ws/src/testpkg_action/')
# import Fibonacci
from action import *
# import Fibonacci.action

class FibonacciActionServer(Node):
    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        return Fibonacci.Result()

def main(args=None):
    rclpy.init(args=args)
    fibonacci_action_server = FibonacciActionServer()
    rclpy.spin(fibonacci_action_server)

if __name__ == '__main__':
    main()