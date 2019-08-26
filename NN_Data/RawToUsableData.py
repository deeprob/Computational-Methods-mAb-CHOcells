
# coding: utf-8

# In[6]:


'''To use this function, you will need to have all the data in the dataset as 
multiple Pandas Dataframe objects. For example the Glucose Concentration data will have to
be a Pandas Dataframe that has concentrations of the glucose at specific time 
intervals.This function will return all the features as a normalized matrix of 
values.'''

import numpy as np

class UsableData:
    def __init__(self,glycan,*args):
        self.rawfeatures = [*args]
        self.glycan = glycan
        self.X = self.getX()
        self.y = self.getY()
    
    def normalize(self,df):
        dfmax = df.max(axis=1).replace(0,1)
        newdf = df.astype(float).divide(dfmax,axis=0)
        return newdf


    def normalizeGlycan(self,df):
        return df.apply(lambda x: x/100)
    
    def getX(self):
        
        features = []
        for i in self.rawfeatures:
            features.append(self.normalize(i))
            
        X = features[0].values.astype(float)
        for i in features[1:]:
            X = np.append(X,i.values.astype(float),axis=1)
            
        return X
    
    def getY(self):
        return self.normalizeGlycan(self.glycan).values.astype(float)
        
    

