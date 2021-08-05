import pandas as pd
import numpy as np

class Pinguins_ml:
    
    def __init__(self, df, target):
        #--------------------------------------------------------
        """ • Initialise self.df, self.X, self.y
            • Params = df, target
            • Return None """
        #---------------------------------------------------------
        self.df = df
        self.target = target