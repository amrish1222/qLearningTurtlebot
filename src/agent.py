import numpy as np
from qTable import qt
class qAgent():
    def __init__(self):
        # self.rospy.init_node('qAgent')
        self.turtleName = ""
        self.velocityTopic = '/mobile_base/commands/velocity'
        self.totalReward = 0
        self.qTable = dict()
        
    def doAction(self):
        pass
    
    def getAction(self):
        pass
    
    def learn(self, 
              prevStateIndex,
              prevAction,
              currentState,
              reward):
        pass
    
    