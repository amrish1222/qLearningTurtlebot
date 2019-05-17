import rospy
import numpy as np
import random
import copy
import pickle
import os

import rospkg

# get an instance of RosPack with the default search paths
rospack = rospkg.RosPack()

# list all packages, equivalent to rospack list
rospack.list() 


class qTable:
    def __init__(self,
                 _numActions,
                 _learningFactor = 0.2,
                 _discountFactor = 0.5,
                 _epsilon = 0.5):

        self.numActions = _numActions
        self.alpha = _learningFactor
        self.gamma = _discountFactor
        self.epsilon = _epsilon
        self.defaultActWt = self.getDefaultActionWeights()
        self.getActionDict()
        self.qTable = dict()

    def getActionDict(self):
        self.actionDict = dict()
        for ndx in range(self.numActions):
            self.actionDict[ndx] = ndx

    def getDefaultActionWeights(self):
        return tuple([1/self.numActions]*self.numActions)

    def updateTable(self,
                    prevState,
                    prevAction,
                    currState,
                    reward):
        #use defaut if not found
        qPrevAll = list(self.qTable.setdefault(prevState, self.defaultActWt))
        prevActNdx = self.actionDict[prevAction]
        qPrev = qPrevAll[prevActNdx]
        qPrevMax  = max(self.qTable.setdefault(currState, self.defaultActWt))
        qNew = qPrev + self.alpha * (reward + self.gamma* qPrevMax - qPrev)
        qPrevAll[prevActNdx] = qNew
        self.qTable[prevState] = tuple(qPrevAll)

    def eGreedyPolicy(self,
                      currState):
        possibleActions = self.actionDict.values()
        qVals = self.qTable.setdefault(currState, self.defaultActWt)
        posQvals = [qVals[self.actionDict[act]] for act in possibleActions]
        maxNdx = posQvals.index(max(posQvals))
        maxAct = possibleActions[maxNdx]
        finalAct = 0
        if random.random() <= self.epsilon:
            finalAct = maxAct
        else:
            finalAct = possibleActions.pop(maxNdx)
            if len(possibleActions) == 1 :
                finalAct = possibleActions[-1]
            elif len(possibleActions) > 1:
                finalAct = possibleActions[random.randint(0,len(possibleActions)-1)]
        return finalAct
        
    def saveQt(self):
        rospack = rospkg.RosPack()
        rospack.list() 
        filename = rospack.get_path('qLearningTurtlebot')
        with open(filename+'/qTable/filename.pickle', 'wb') as handle:
            pickle.dump(self.qTable , handle, protocol=pickle.HIGHEST_PROTOCOL)
            
    def loadQt(self):
#        with open('/home/amrish/Documents/filename.pickle', 'rb') as handle:
        rospack = rospkg.RosPack()
        rospack.list() 
        filename = rospack.get_path('qLearningTurtlebot')
        with open(filename+'/qTable/Maze3.pickle', 'rb') as handle:    
            self.qTable = pickle.load(handle)
            
    def loadSeedQt(self):
        rospack = rospkg.RosPack()
        rospack.list() 
        filename = rospack.get_path('qLearningTurtlebot')
        exists = os.path.isfile(filename+'/qTable/seed.pickle')
        if exists:
            with open(filename+'/qTable/seed.pickle', 'rb') as handle:
                self.qTable = pickle.load(handle)
                self.epsilon = 0.7