import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/unghui/turtlebot_says_ros2_ws/install/ts_english'
