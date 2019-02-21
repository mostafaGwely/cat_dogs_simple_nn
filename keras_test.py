
# coding: utf-8

# In[3]:


import argparse


# In[4]:


ap = argparse.ArgumentParser()
ap.add_argument('-d','--dataset',required=True,help="path to input dataset of images")
ap.add_argument('-m','--model',required=True,help="path to the output trained model")
ap.add_argument('-l','--label-bin',required=True,help="path to output label binarize")
ap.add_argument('-p','--plot',required=True,help='path to the output accuracy/loss plot')
args = vars(ap.parse_args())

