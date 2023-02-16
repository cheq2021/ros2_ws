# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import numpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose, PoseStamped


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        self.declare_parameter('position_x', 0.00)
        self.declare_parameter('position_y', 0.00)
        self.declare_parameter('position_z', 0.00)
        self.declare_parameter('orientation_x', 0.00)
        self.declare_parameter('orientation_y', 0.00)
        self.declare_parameter('orientation_z', 0.00)
        self.declare_parameter('orientation_w', 0.00)

        msg = PoseWithCovarianceStamped()
        msg.header.frame_id = 'map'
        msg.pose.pose.position.x = self.get_parameter('position_x').get_parameter_value().double_value
        msg.pose.pose.position.y = self.get_parameter('position_y').get_parameter_value().double_value
        msg.pose.pose.position.z = self.get_parameter('position_z').get_parameter_value().double_value
        msg.pose.pose.orientation.x = self.get_parameter('orientation_x').get_parameter_value().double_value
        msg.pose.pose.orientation.y = self.get_parameter('orientation_y').get_parameter_value().double_value
        msg.pose.pose.orientation.z = self.get_parameter('orientation_z').get_parameter_value().double_value
        msg.pose.pose.orientation.w = self.get_parameter('orientation_w').get_parameter_value().double_value
        msg.pose.covariance =  numpy.array([
            0.25, 0.0, 0.0,  0.0,  0.0,  0.0,
            0.0, 0.25, 0.0,  0.0,  0.0,  0.0,
            0.0, 0.0, 0.0, 0.0,  0.0,  0.0,
            0.0, 0.0, 0.0,  0.0, 0.0,  0.0,
            0.0, 0.0, 0.0,  0.0,  0.0, 0.0,
            0.0, 0.0, 0.0,  0.0,  0.0,  0.06853891909122467,
        ])

        self.publisher = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
