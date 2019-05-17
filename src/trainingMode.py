#! /usr/bin/env python

import rospy
import sensor_msgs.msg
from nav_msgs.msg import Odometry

import numpy as np
from agent import qAgent
#from geometry_msgs.msg import Twist
#from std_msgs.msg import Int64

import matplotlib.pyplot as plt

plt.ion()
fig, ax = plt.subplots()
x, y = [],[]
xPlot, yPlot = [],[]
sc = ax.plot(x,y)
plt.xlim(-150,2000)
plt.ylim(-150,1000)
plt.draw()


from environment import turtleBotEnv
from qTable import qTable
from game import playGame


rospy.init_node('trainingMode', log_level = rospy.DEBUG, anonymous = True)
rospy.loginfo("node Created")
env = turtleBotEnv()
qA1 = qAgent(env)
rospy.Subscriber("scan", sensor_msgs.msg.LaserScan , qA1.LaserScanProcess)
rospy.Subscriber('odom',Odometry,qA1.odometry)
#rewardPub = rospy.Publisher('/reward', Int64, queue_size=10)
qt = qTable(env.numActions)
game = playGame(env, qA1, qt)
cummulativeReward = []
rospy.loginfo("Variables Initialized")

qt.loadSeedQt()
print(qt.qTable)

for i in range(10000):
    rospy.loginfo("Game number= "+ str(i))
    reward = game.runGame()
#    cummulativeReward.append(game.runGame())
    
    xPlot.append(i)
    yPlot.append(reward)
#    
#    sc.set_offsets(np.c_[xPlot,yPlot])
#    fig.canvas.draw_idle()
#    plt.pause(0.1)
#    
#    plt.show()
    if i %2 ==0:
#        sc.set_offsets(np.c_[xPlot,yPlot])
        plt.plot(xPlot,yPlot, 'b-')
        fig.canvas.draw_idle()
        plt.pause(0.1)
        plt.show()
        xPlot = xPlot[-1:]
        yPlot = yPlot[-1:]
    
    if i % 50 == 0:
        qt.saveQt()
        print(cummulativeReward)
        
        if qt.epsilon < 9.95:
            qt.epsilon += 0.05
    pass
