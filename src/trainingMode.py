#! /usr/bin/env python

import rospy
import sensor_msgs.msg
from agent import qAgent
from geometry_msgs.msg import Twist

def callback(data):
    print("hellom")

rospy.init_node('trainingMode', log_level = rospy.DEBUG, anonymous = True)
qA1 = qAgent()
rospy.Subscriber("scan", sensor_msgs.msg.LaserScan , qA1.LaserScanProcess)
print("hellom")
r =  rospy.Rate(1)
while not rospy.is_shutdown():
    rospy.loginfo("hellomain")
    qA1.doAction()
    r.sleep()
#rospy.spin()