
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
GenmAb_data_CDOpticho = pd.read_excel(r'C:\Users\deeprob\Chemical Projects\Bio-modelling\NN_Data\Yu-DoE-data-compilation_LS.xlsx',skiprows=2)


# In[35]:


#GenmAb_data_CDOpticho


# In[36]:


#media concentration parsing function
def parsingfunction(df,row1,row2,col1,col2):
    newdf = df.iloc[row1:row2,col1+1:col2]
    newdf.columns = ['D0','D2','D4','D7']
    newdf = newdf.reset_index(drop=True)
    return newdf.diff(axis=1).drop(columns=['D0'])


# In[37]:


#supplement parsing function -- 0 for NH4Cl; 1 for Gln; 2 for Asn
def parsingfunctionsupp(df,row1,row2,col1,n):
    if n ==0:
        column = 'NH4Cl'
    elif n ==1:
        column = 'Gln'
    else:
        column = 'Asn'
    return pd.DataFrame(list(map(lambda x1: x1[n],list(map(lambda x: x.split(','),df.iloc[row1:row2,col1])))),columns=[column])
    


# In[38]:


TCD_CD = parsingfunction(GenmAb_data_CDOpticho,2,18,1,6)


# In[39]:


VCD_CD = parsingfunction(GenmAb_data_CDOpticho,2,18,7,12)


# In[40]:


Glucose_CD = parsingfunction(GenmAb_data_CDOpticho,2,18,13,18)


# In[41]:


Lactate_CD = parsingfunction(GenmAb_data_CDOpticho,2,18,19,24)


# In[42]:


Ammonia_CD = parsingfunction(GenmAb_data_CDOpticho,2,18,25,30)


# In[43]:


IgG_CD = parsingfunction(GenmAb_data_CDOpticho,2,18,31,36)


# In[44]:


Glutamine_CD = parsingfunction(GenmAb_data_CDOpticho,24,40,1,6)


# In[45]:


NH4Cl_CD = parsingfunctionsupp(GenmAb_data_CDOpticho,2,18,1,0)


# In[46]:


Gln_CD = parsingfunctionsupp(GenmAb_data_CDOpticho,2,18,1,1)


# In[47]:


Asn_CD = parsingfunctionsupp(GenmAb_data_CDOpticho,2,18,1,2)


# In[60]:


# GLycan Function
Glycan_CD = pd.DataFrame(GenmAb_data_CDOpticho.iloc[24:40,8:21]).replace(np.nan,0)
Glycan_CD.columns = list(GenmAb_data_CDOpticho.iloc[23,8:21])
Glycan_CD = Glycan_CD.reset_index(drop=True)


# In[61]:


#Glycan_CD

