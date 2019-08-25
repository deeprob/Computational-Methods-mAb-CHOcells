# Computational Methods for Robust Bio-processing
This project accounts for my Master's thesis at Carnegie Mellon University 
# Project aim
The goal of this project is to develop a hybrid model of glycosylation in Monoclonal Antibodies (mAbs) produced in Chinese Hamster Ovary Cells. Here I looked at the advantages and disadvantages of both Physics based and Machine Learning based methods of modelling and finally come up with a hybrid model that predicts the relative glycan distribution in mAbs.
# Why is this project useful?
Monoclonal antibodies (mAbs) are a class of commercially valuable biopharmaceuticals that are used for treating diseases such as psoriasis, rheumatoid arthritis and multiple types of cancer. Maintaining the desired product quality of mAbs in the presence of process variations during manufacturing has been difficult for a variety of reasons. One of them is the lack of a robust dynamic mathematical model that can be generalized to different experimental conditions, media supplements and cell lines. According to me, this has mainly been due to the fact that physics based models need to be adjusted everytime there is even a tiny change in environmental conditions or when we vary the initial concentrations of the media or even when we use different supplements or cell-lines. Therefore (also since it's much more exciting) I have turned to Machine Learning based methods of modelling to fill that gap.
# Why have I looked at glycosylation?
Glycosylation is one of the most important determinant of mAb product quality. 
# Why Chinese Hamster Ovary cell lines?
While therapeutic mAbs can be synthesized in several different mammalian cell expression systems such as Chinese Hamster Ovary (CHO) cell lines, murine myeloma cell lines NS0, Sp2/0, over half of all currently approved mAbs are produced in Chinese Hamster Ovary (CHO) cell lines (data accessed online from Drugs@FDA).
# What files does it have at this moment?
Currently, I have developed a Macroscale model that takes initial concentrations of the different media of a particular cell line, the total cell density, the viable cell density, the antibody concentration and the total time span of experiments and it predicts the change of concentration of all those factors with time. In addition to that, I have also developed a separate Artificial Neural Network based model that takes in all the factors mentioned above throughout the whole time-span of the experiment and predicts the final relative glycan distribution of mAb. This model can also take in the values of different supplements added throughout the course of the experiment. As of this moment it is only compatible with 3 types of supplements: NH4cl, Gln, Asn. It is also agnostic to CDOptiCHO or AMBIC cell-line.
# What files will I add eventually?
1. While I have added a basic 1-hidden layer Neural Network model that is coded from scratch, I will add a more advanced multiple hidden layer Neural Network model.
2. Right now, the model is static. I plan to make it dynamic with the help of a time series model. This will also be added soon.
3. One of the reasons why I want the model to be dynamic is that I can control it using Reinforcement Learning. I will look into that in the future. 
# Licensing and rights.
As of this moment, this is not an open-source project. So you can admire or criticize the model or the data but you cannot copy, modify or use it for your own benefit. But eventually, I will make it open-source.  
