
# coding: utf-8

# In[4]:
''' The model parameters are adopted from a dissertation submitted by Devesh Radhakrishnan '''

#model parameters

Yxglc = 1.4e9        # Yield coefficient biomass on glucose 
Yxgln = 2.7e9        # Yield coefficient biomass on glutamine
Yxlac = 6.53e7       # Yield coefficient biomass on lactate
Yammgln = 0.63       # Yield coefficient ammonia on glutamine
Ylacglc = 1.3        # Yield coefficient lactate on glucose
Ymabglc = 5.55e-3    # Yield coefficient mab on glucose
Kdgln = 9.6e-3       # Constant for glutamine degradation
Kglc = 0.14          # Monod constant for glucose
Klac = 0.25          # Monod constant for glucose
Kgln = 0.025         # Monod constant for glutamine
Kilac = 171.76       # constant for lactate inhibition
Kiamm = 28.48        # constant for ammonia inhibition
Klysis = 0.02        # Cell lysis rate (range between 0.02 to 0.06)
mgln = 4.25e-15      # Glutamine maintenance coefficient
a0 = 2.25e-10        # constant for Glucose maintenance coefficient
a1 = 39.65           # constant for Glucose maintenance coefficient
mumax1 = 0.03        # Maximum growth rate exponential
mumax2 = 6.5e-3      # Maximum growth rate stationary
mudmax = 0.042       # Maximum death rate
kd0 = 4.54e-4        # Death rate constant
kd1 = 5e-3           # Death rate constant
k = 0.08             # self defined constant


# In[5]:


# experimental parameters
# conc in mM; time in hr; mass in g; Volume in L

V = 50e-3 #Ltr
 
