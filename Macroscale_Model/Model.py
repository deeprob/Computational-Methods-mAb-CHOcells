
# coding: utf-8

# In[1]:


#import model parameters
from .Model_parameters import *

#import the required modules in python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# In[2]:


class mAb_model:
    def __init__(self,Glc0,Gln0,Lac0,Amm0,Xv0,Xt0,Mab0,tfinal):
        self.X0 = np.array([Glc0,Gln0,Lac0,Amm0,Xv0,Xt0,Mab0])
        self.tspan = np.array([0,tfinal])
        self.teval,self.h = np.linspace(*self.tspan,20,retstep=True)
        self.sol = solve_ivp(self.dXdt,self.tspan,self.X0,t_eval=self.teval,max_step=self.h) 
        
    @staticmethod
    def dXdt(t,X):
        Glc,Gln,Lac,Amm,Xv,Xt,Mab = X
        if Gln<1e-3:
            mu = mumax2 * Glc/(Kglc+Glc) * Lac/(Kilac+Lac) * Kiamm/(Kiamm+Amm)
            qcons = mu/Yxlac
        else:
            mu = mumax1 * Glc/(Kglc+Glc) * Gln/(Kgln+Gln) * Kilac/(Kilac+Lac) * Kiamm/(Kiamm+Amm)
            qcons = 0.5e-11       #modified value
        mud = mudmax * kd0/(kd1+mu)
        dXvdt = (mu - mud)*Xv
        dXtdt = mu*Xv - Klysis*(Xt-Xv)
        mglc = a0*Glc/(a1+Glc)
        qglc = mu/Yxglc + mglc
        dGlcdt = -qglc*Xv
        qgln = mu/Yxgln + mgln
        dGlndt = -qgln*Xv - Kdgln*Gln
        qlac = Ylacglc*qglc
        dLacdt = qlac*Xv - qcons*Xv*Lac/(k*Glc)
        qamm = Yammgln * qgln
        dAmmdt = qamm*Xv + Kdgln*Gln
        qmab = Ymabglc*qglc
        dMabdt = qmab*Xv
        return np.array([dGlcdt,dGlndt,dLacdt,dAmmdt,dXvdt,dXtdt,dMabdt])
    
    def plotMediaConc(self):
        plt.figure(figsize=(20,10))
        plt.subplot(2,2,1)
        plt.plot(self.teval,self.sol.y[0])
        plt.xlabel('time in hr')
        plt.ylabel('Glucose')

        plt.subplot(2,2,2)
        plt.plot(self.teval,self.sol.y[1])
        plt.xlabel('time in hr')
        plt.ylabel('Glutamine')

        plt.subplot(2,2,3)
        plt.plot(self.teval,self.sol.y[2])
        plt.xlabel('time in hr')
        plt.ylabel('Lactate')

        plt.subplot(2,2,4)
        plt.plot(self.teval,self.sol.y[3])
        plt.xlabel('time in hr')
        plt.ylabel('Ammonia');
        
    def plotTCDVCD(self):
        plt.plot(self.teval,self.sol.y[4],label='Xv')
        plt.plot(self.teval,self.sol.y[5],label='Xt')
        plt.xlabel('time in hr')
        plt.ylabel('X')
        plt.legend()
        plt.title('Viable and Total Cell Density');
        
    def plotAntibodyConc(self):
        plt.plot(self.teval,self.sol.y[6])
        plt.xlabel('time in hr')
        plt.ylabel('MAB')
        plt.title('MAB Concentration');
        


  

