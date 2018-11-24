#!/usr/bin/env python
import cv2
import cv_bridge
import rospy
import sys
import os
from sensor_msgs.msg import Image


class DoMagic:
  def __init__(self):
    rospy.init_node('magical_node', anonymous=True)

    # self.image_input_name = rospy.resolve_name('/camera/depth/image_rect_raw')

    image_sub = rospy.Subscriber(self.image_input_name, Image, self.callback)
    self.bridge = cv_bridge.CvBridge()
    self.ctr = 0
    self.image = None

  def callback(self, msg):
    


if __name__ == '__main__':
  node = DoMagic()
  rospy.spin()
