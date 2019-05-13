import rospy
import random
import numpy as np
import math

from std_msgs.msg import String
import sensor_msgs.msg
from geometry_msgs.msg import Twist
import random

#from qTable import qt

class qAgent():
    def __init__(self):
        # self.rospy.init_node('qAgent')
        self.turtleName = ""
        self.velocityTopic = '/mobile_base/commands/velocity'
        self.totalReward = 0
        self.qTable = dict()
        self.velPub = rospy.Publisher(self.velocityTopic, Twist, queue_size=10)
        self.isCollision = False
        self.LINX = 0.0 #Always forward linear velocity.
        self.minRange = 0.6 #THRESHOLD value for laser scan.
        self. currentState = []
    def doAction(self):
        twist = self.genActionMsg(random.randint(0,2))
        rospy.loginfo(twist)
        self.velPub.publish(twist)
    
    def getAction(self):
        pass
    
    def learn(self, 
              prevStateIndex,
              prevAction,
              currentState,
              reward):
        pass
    
    def genActionMsg(self,actionIndex):
        twist = Twist()
        if actionIndex == 0:
            twist.linear.x = 0.2
            twist.angular.z = 0
        elif actionIndex == 1:
            twist.linear.x = 0.05
            twist.angular.z = 0.3
        elif actionIndex == 2:
            twist.linear.x = 0.05
            twist.angular.z = 0.3
        else:
            twist.linear.x = 0
            twist.angular.z = 0
        return twist
    
    def LaserScanProcess(self, data):
        self.isCollision = False
        state = []        
        mod = round(len(data.ranges)/4)
        for ndx,val in enumerate(data.ranges):
            if ndx % mod == 0:
                if math.isnan(val):
                    state.append(6)
                else:
                    state.append(val)
            if val < self.minRange:
                self.isCollision = True
        self.currentState = state