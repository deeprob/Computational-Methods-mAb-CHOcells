
# coding: utf-8

# In[1]:


from .Data_DoE_GenmAb_Ambic import *
from .Data_DoE_GenmAb_CDOptiCHO import *


# In[11]:


''' The two data files imported above has TCD,VCD,Glucose,Lactate,
Ammonia,IgG,Glutamine,NH4Cl,Gln,Asn concentration throughout the span of the 
experiment that is for Day0, Day2, Day4 and Day7 as pandas Dataframe for two
different cell lines, AMBIC and CDOptiCHO. In addition to that, they also have
the final glycan concentration for both cell lines. I will combine the raw data 
from both the datasets to obtain a single dataset with all the required data.
Then I will take 80% of the data to train a model and the rest of it to test 
that model. The division will function is in a separate file.'''

#For the media concentration and supplements 
TCD = TCD_CD.append(TCD_Amb[8:]).reset_index(drop=True)
VCD = VCD_CD.append(VCD_Amb[8:]).reset_index(drop=True)
Glucose = Glucose_CD.append(Glucose_Amb[8:]).reset_index(drop=True)
Lactate = Lactate_CD.append(Lactate_Amb[8:]).reset_index(drop=True)
Ammonia = Ammonia_CD.append(Ammonia_Amb[8:]).reset_index(drop=True)
IgG = IgG_CD.append(IgG_Amb[8:]).reset_index(drop=True)
Glutamine = Glutamine_CD.append(Glutamine_Amb[0:8].fillna(1150)).reset_index(drop=True)
NH4Cl = NH4Cl_CD.append(NH4Cl_Amb[8:]).reset_index(drop=True)
Gln = Gln_CD.append(Gln_Amb[8:]).reset_index(drop=True)
Asn = Asn_CD.append(Asn_Amb[8:]).reset_index(drop=True)

# For the Glycan
Glycan = Glycan_CD.iloc[:,0:9].append(Glycan_Amb.iloc[8:,0:9]).reset_index(drop=True)


# In[16]:


from .RawToUsableData import UsableData


# In[17]:


myData = UsableData(Glycan,TCD,VCD,Glucose,Lactate,Ammonia,IgG,Glutamine,NH4Cl,Gln,Asn)

