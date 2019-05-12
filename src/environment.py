import numpy as np
import rospy
from std_srvs.srv import Empty

class turtleBotEnv():
    def __init__(self):
        self.stateDict = dict()
        self.actions = []
        self.numStates = 0
        self.numActions = 0
        #self.rospy.init_node('turtleBotEnv_node')
        self.resetWorldTopic = '/gazebo/reset_world'
        self.pauseTopic = '/gazebo/pause_physics'
        self.unPauseTopic = '/gazebo/unpause_physics'
        self.reset_world = rospy.ServiceProxy(self.resetWorldTopic, Empty)
        self.pause_world = rospy.ServiceProxy(self.pauseTopic, Empty)
        self.unPause_world = rospy.ServiceProxy(self.unPauseTopic, Empty)
        self.genStates()
        self.genActions()
        
        
    def genStates(self):
        index = -1
        self.stateDict = dict()
        for i in range(6):
            for j in range(6):
                for k in range(6):
                    for l in range(6):
                        index+=1
                        self.stateDict[(i,j,k,l)] = index
        self.numStates = index
    
    def genActions(self):
        tempAction = []
        for i in range(3):
            tempAction.append(i)
        self.actions = tempAction
        self.numActions = 3
    
    def getStateIndex(self, state):
        return self.stateDict[state]
    
    def envReset(self):
        rospy.wait_for_service(self.resetWorldTopic)
        self.reset_world()
    
    def envPause(self):
        rospy.wait_for_service(self.pauseTopic)
        self.pause_world()
        
    def envUnPause(self):
        rospy.wait_for_service(self.unPauseTopic)
        self.unPause_world()