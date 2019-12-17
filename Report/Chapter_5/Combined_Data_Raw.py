#!/usr/bin/env python
# coding: utf-8

# In[69]:


from Data_DoE_GenmAb_Ambic import *
from Data_DoE_GenmAb_CDOptiCHO import *

Glucose = pd.concat([Glucose_Amb,Glucose_CD],axis=0).reset_index(drop=True).astype(float)
Glutamine = pd.concat([Glutamine_Amb,Glutamine_CD],axis=0).reset_index(drop=True).astype(float)
Lactate = pd.concat([Lactate_Amb,Lactate_CD],axis=0).reset_index(drop=True).astype(float)
Ammonia = pd.concat([Ammonia_Amb,Ammonia_CD],axis=0).reset_index(drop=True).astype(float)
TCD = pd.concat([TCD_Amb,TCD_CD],axis=0).reset_index(drop=True).astype(float)
VCD = pd.concat([VCD_Amb,VCD_CD],axis=0).reset_index(drop=True).astype(float)
IgG = pd.concat([IgG_Amb,IgG_CD],axis=0).reset_index(drop=True).astype(float)


# In[31]:


myFeatures = pd.concat([Glucose,Glutamine,Lactate,Ammonia,TCD,VCD,IgG],axis=1).astype(float)
myOutputs = pd.concat([Glycan_Amb,Glycan_CD],axis=0).astype(float)
