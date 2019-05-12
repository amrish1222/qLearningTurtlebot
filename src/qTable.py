import numpy as np

class qt():
    def __init__(self,
                 _numStates,
                 _numActions):
        self.qtable = dict()