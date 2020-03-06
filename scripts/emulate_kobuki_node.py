#!/usr/bin/env python3

import sys
import time

import rclpy

from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

def main():
    rclpy.init(args=sys.argv)

    node = rclpy.create_node('emulate_kobuki_node')

    imu_publisher = node.create_publisher(Imu, 'imu_data', 0)
    odom_publisher = node.create_publisher(Odometry, 'odom', 0)

    imu_msg = Imu()
    odom_msg = Odometry()
    counter = 0
    while True:
        counter += 1
        now = time.time()
        if (counter % 50) == 0:
            odom_msg.header.stamp.sec = int(now)
            odom_msg.header.stamp.nanosec = int(now * 1e9) % 1000000000
            odom_publisher.publish(odom_msg)
        if (counter % 100) == 0:
            imu_msg.header.stamp.sec = int(now)
            imu_msg.header.stamp.nanosec = int(now * 1e9) % 1000000000
            imu_publisher.publish(imu_msg)
            counter = 0
        time.sleep(0.001)


if __name__ == '__main__':
    sys.exit(main())