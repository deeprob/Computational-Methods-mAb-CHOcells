
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
GenmAb_data_AMBIC = pd.read_excel(r'C:\Users\deeprob\Chemical Projects\Bio-modelling\NN_Data\Yu-DoE-data-compilation_LS.xlsx',sheet_name='GenmAb AMBIC',skiprows=2)


# In[4]:


#GenmAb_data_AMBIC


# In[5]:


#media concentration parsing function
def parsingfunction(df,row1,row2,col1,col2):
    newdf = df.iloc[row1:row2,col1+1:col2]
    newdf.columns = ['D0','D2','D4','D7']
    newdf = newdf.reset_index(drop=True)
    return newdf.diff(axis=1).drop(columns=['D0'])


# In[6]:


#supplement parsing function -- 0 for NH4Cl; 1 for Gln; 2 for Asn
def parsingfunctionsupp(df,row1,row2,col1,n):
    if n ==0:
        column = 'NH4Cl'
    elif n ==1:
        column = 'Gln'
    else:
        column = 'Asn'
    return pd.DataFrame(list(map(lambda x1: x1[n],list(map(lambda x: x.split(','),df.iloc[row1:row2,col1])))),columns=[column])
    


# In[12]:


TCD_Amb = parsingfunction(GenmAb_data_AMBIC,3,19,1,6)


# In[14]:


VCD_Amb = parsingfunction(GenmAb_data_AMBIC,3,19,7,12)


# In[15]:


Glucose_Amb = parsingfunction(GenmAb_data_AMBIC,3,19,13,18)


# In[17]:


Lactate_Amb = parsingfunction(GenmAb_data_AMBIC,3,19,19,24)


# In[18]:


Ammonia_Amb = parsingfunction(GenmAb_data_AMBIC,3,19,25,30)


# In[19]:


IgG_Amb = parsingfunction(GenmAb_data_AMBIC,3,19,31,36)


# In[26]:


Glutamine_Amb = parsingfunction(GenmAb_data_AMBIC,22,38,1,6)


# In[28]:


NH4Cl_Amb = parsingfunctionsupp(GenmAb_data_AMBIC,3,19,1,0)


# In[29]:


Gln_Amb = parsingfunctionsupp(GenmAb_data_AMBIC,3,19,1,1)


# In[30]:


Asn_Amb = parsingfunctionsupp(GenmAb_data_AMBIC,3,19,1,2)


# In[36]:


# GLycan Function
Glycan_Amb = pd.DataFrame(GenmAb_data_AMBIC.iloc[22:38,8:21]).replace(np.nan,0)
Glycan_Amb.columns = list(GenmAb_data_AMBIC.iloc[21,8:21])
Glycan_Amb = Glycan_Amb.reset_index(drop=True)


# In[37]:


#Glycan_Amb

