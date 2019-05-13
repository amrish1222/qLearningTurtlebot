#! /usr/bin/env python

import rospy
import sensor_msgs.msg
import numpy as np
from agent import qAgent
#from geometry_msgs.msg import Twist
#from std_msgs.msg import Int64

import matplotlib.pyplot as plt

plt.ion()
#fig, ax = plt.subplots()
#x, y = [],[]
#xPlot = []
#yPlot = []
#sc = ax.scatter(x,y)
#plt.xlim(-100,100)
#plt.ylim(-100,100)
#plt.draw()


from environment import turtleBotEnv
from qTable import qTable
from game import playGame


rospy.init_node('trainingMode', log_level = rospy.DEBUG, anonymous = True)
rospy.loginfo("node Created")
env = turtleBotEnv()
qA1 = qAgent(env)
rospy.Subscriber("scan", sensor_msgs.msg.LaserScan , qA1.LaserScanProcess)
#rewardPub = rospy.Publisher('/reward', Int64, queue_size=10)
qt = qTable(env.numActions)
game = playGame(env, qA1, qt)
cummulativeReward = []
rospy.loginfo("Variables Initialized")
for i in range(10000):
    rospy.loginfo("Game number= "+ str(i))
    reward = game.runGame()
#    cummulativeReward.append(game.runGame())
    
#    xPlot.append(i)
#    yPlot.append(reward)
#    
#    sc.set_offsets(np.c_[xPlot,yPlot])
#    fig.canvas.draw_idle()
#    plt.pause(0.1)
#    
#    plt.show()
    plt.plot(i,reward,'-r', linewidth = 10)
    plt.plot(i,reward,'-g', linewidth = 1)
#    plt.axis("equal")
    plt.draw()
    plt.pause(0.00000001)
    
    
    if i % 50 == 0:
        qt.saveQt()
        print(cummulativeReward)
        
        if qt.epsilon > 0.05:
            qt.epsilon += 0.05
    pass
