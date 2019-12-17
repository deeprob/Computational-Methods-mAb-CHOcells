
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
GenmAb_data_AMBIC = pd.read_excel(r'C:\Users\deeprob\Chemical Projects\Bio-modelling\Report\Chapter_7\Yu-DoE-data-compilation_LS.xlsx',sheet_name='GenmAb AMBIC',skiprows=2)


# In[4]:


#GenmAb_data_AMBIC


# In[5]:


#media concentration parsing function
def parsingfunction(df,row1,row2,col1,col2,name=None):
    newdf = df.iloc[row1:row2,col1+1:col2]
    newdf.columns = [f"{name}_D0",f"{name}_D2",f"{name}_D4",f"{name}_D7"]
    newdf = newdf.reset_index(drop=True)
    return newdf#.diff(axis=1).drop(columns=['D0'])


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


TCD_Amb = parsingfunction(GenmAb_data_AMBIC,11,19,1,6,'TCD')


# In[14]:


VCD_Amb = parsingfunction(GenmAb_data_AMBIC,11,19,7,12,'VCD')


# In[15]:


Glucose_Amb = parsingfunction(GenmAb_data_AMBIC,11,19,13,18,'Glucose')


# In[17]:


Lactate_Amb = parsingfunction(GenmAb_data_AMBIC,11,19,19,24,'Lactate')


# In[18]:


Ammonia_Amb = parsingfunction(GenmAb_data_AMBIC,11,19,25,30,'Ammonia')


# In[19]:


IgG_Amb = parsingfunction(GenmAb_data_AMBIC,11,19,31,36,'IgG')


# In[26]:


Glutamine_Amb = parsingfunction(GenmAb_data_AMBIC,22,30,1,6,'Glutamine').fillna(1150.0)


# In[28]:


NH4Cl_Amb = parsingfunctionsupp(GenmAb_data_AMBIC,3,19,1,0)


# In[29]:


Gln_Amb = parsingfunctionsupp(GenmAb_data_AMBIC,3,19,1,1)


# In[30]:


Asn_Amb = parsingfunctionsupp(GenmAb_data_AMBIC,3,19,1,2)


# In[36]:


# GLycan Function
Glycan_Amb = pd.DataFrame(GenmAb_data_AMBIC.iloc[30:38,8:17]).replace(np.nan,0)
Glycan_Amb.columns = list(GenmAb_data_AMBIC.iloc[21,8:17])
Glycan_Amb = Glycan_Amb.reset_index(drop=True)

# Grouped Glycan Function
Glycan_Amb_grp = pd.DataFrame(GenmAb_data_AMBIC.iloc[30:38,17:20]).replace(np.nan,0)
Glycan_Amb_grp.columns = list(GenmAb_data_AMBIC.iloc[21,17:20])
Glycan_Amb_grp = Glycan_Amb_grp.reset_index(drop=True)

# Fucose Function
Glycan_Amb_fuc = pd.DataFrame(GenmAb_data_AMBIC.iloc[30:38,20]).replace(np.nan,0)
Glycan_Amb_fuc.columns = [GenmAb_data_AMBIC.iloc[21,20]]
Glycan_Amb_fuc = Glycan_Amb_fuc.reset_index(drop=True)


# In[37]:


#Glycan_Amb

