import rospy
import sensor_msgs.msg

import numpy as np

from environment import turtleBotEnv
from agent import qAgent

class playGame():
    def __init__(self,
                 _env,
                 _agent,
                 _qClass):
        self.env = _env
        self.agent = _agent
        self.qClass = _qClass
        self.learning = True

        
    def runGame(self):
        rospy.loginfo("Game Started")
        self.agent.reset()
        self.env.envReset()
        count = 0
#        self.env.envUnPause()
        r = rospy.Rate(10)
        while count<2000 and not self.agent.isCollision and not rospy.is_shutdown():
            rospy.loginfo("Game Iteration: " + str(count))
#            self.env.envUnPause()
            action = self.agent.getAction(self.qClass,self.agent.currentState)
            prevState = self.agent.currentState
            print("action :", action)
            self.agent.doAction(action)
            r.sleep()
            try:
                rospy.wait_for_message("/scan",sensor_msgs.msg.LaserScan,1.0)
            except rospy.exceptions.ROSException:
                rospy.loginfo("waiting for scan data")
#            self.env.envPause()
            if self.learning:
                reward = self.agent.getReward(action)
                self.agent.totalReward += reward
                self.qClass.updateTable(prevState,action,self.agent.currentState,reward)
            count+=1
#            rospy.spinOnce()
        rospy.loginfo("game ended")
        return self.agent.totalReward