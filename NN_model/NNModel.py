
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


class NeuralNetwork:
    def __init__(self,X,y,hidden_units=5,lr=0.5):
        self.X = X
        self.y = y
        self.hidden_units = hidden_units
        self.lr = lr
        self._X = np.insert(X,[0],1,axis=1)
        self.alpha = np.random.uniform(-0.1,0.1,(self.hidden_units,len(self._X[0])))
        self.beta = np.random.uniform(-0.1,0.1,(len(self.y[0]),self.hidden_units+1))

    def NNforward(self,X_1,y_1):
        a = np.dot(self.alpha,np.reshape(X_1,(len(X_1),1)))
        z = 1/(1+np.exp(-a))
        Z = np.insert(z,0,1)
        b = np.dot(self.beta,np.reshape(Z,(len(Z),1)))
        yhat = 1/(1+np.exp(-b))
        y_1 = np.reshape(y_1,(len(y_1),1))
        J = np.sum((y_1-yhat)**2)/2
        return J,yhat,b,Z,z,a
    
    def NNbackward(self,J,yhat,b,Z,z,a,y_1,alpha,beta,X_1):
        y_1 = np.reshape(y_1,(len(y_1),1))
        dJdyhat = (yhat-y_1)
        dJdb = yhat*(1-yhat)*dJdyhat
        dJdbeta = np.dot(dJdb,np.reshape(Z,(1,len(Z))))
        dJdz = np.dot(beta[:,1:].T,dJdb)
        dJda = dJdz*z*(1-z)
        dJdalpha = np.dot(dJda,np.reshape(X_1,(1,len(X_1))))
        return dJdalpha,dJdbeta
    
    def train(self,epoch,error):
        e = 0
        allJ = 1e9
        while e<epoch and allJ>error:
            Jlist = []
            for i,j in zip(self._X,self.y):
                la = self.NNforward(i,j)
                Jlist.append(la[0])
                lo = self.NNbackward(*la,j,self.alpha,self.beta,i)
                self.alpha = self.alpha - self.lr*lo[0]
                self.beta = self.beta - self.lr*lo[1]
            e+=1
            allJ = sum(Jlist)/len(Jlist)
            
    def test(self,X_test,y_test):
        error = []
        pred = []
        X_new = np.insert(X_test,[0],1,axis=1)
        for x,y in zip(X_new,y_test):
            err = self.NNforward(x,y)
            error.append(err[0]*2)
            pred.append(err[1])
        return error,pred
          

