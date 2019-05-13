#! /usr/bin/env python

import rospy
import sensor_msgs.msg
from agent import qAgent
from geometry_msgs.msg import Twist

from environment import turtleBotEnv
from qTable import qTable
from game import playGame


rospy.init_node('trainingMode', log_level = rospy.DEBUG, anonymous = True)
rospy.loginfo("node Created")
env = turtleBotEnv()
qA1 = qAgent(env)
rospy.Subscriber("scan", sensor_msgs.msg.LaserScan , qA1.LaserScanProcess)
qt = qTable(env.numActions)
game = playGame(env, qA1, qt)
rospy.loginfo("Variables Initialized")
for i in range(3000):
    rospy.loginfo("Game number= "+ str(i))
    if qt.epsilon > 0.05:
        qt.epsilon -= 0.005
    game.runGame()
    pass

#==============================================================================
# print("hellom")
# r =  rospy.Rate(1)
# while not rospy.is_shutdown():
#     rospy.loginfo("hellomain")
#     qA1.doAction()
#     r.sleep()
# #rospy.spin()
#==============================================================================
