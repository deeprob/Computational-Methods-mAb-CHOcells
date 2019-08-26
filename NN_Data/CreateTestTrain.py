
# coding: utf-8

# In[ ]:
''' Randomly samples a dataset to create Test and Train data. Here the division is by default 80% train data and 20% test data which can be changed accordingly. It takes in the dataset as a matrix of size p*n where p in the number of samples and n is the number of features. It spills out a randomly sampled dataset divide according to the div variable.''' 

import random
class GenerateTestTrain:
    def __init__(self,_X,_y,div=0.8):
        self._X = _X
        self._y = _y
        self.div = div
        self.Xtrain,self.ytrain,self.Xtest,self.ytest = self.get_train_test()
        
    def random_shuffle(self):
        n = self._X.shape[0]
        a = list(range(n))
        random.shuffle(a)
        return a
    
    def get_train_test(self):
        ridx = self.random_shuffle()
        tridx = int(len(ridx)*self.div)
        Xtrain = self._X[ridx[:tridx]]
        Xtest = self._X[ridx[tridx:]]
        ytrain = self._y[ridx[:tridx]]
        ytest = self._y[ridx[tridx:]]
        return Xtrain,ytrain,Xtest,ytest
        

