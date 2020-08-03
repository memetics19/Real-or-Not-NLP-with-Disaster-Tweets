#!/usr/bin/env python
# coding: utf-8

# In[33]:


# !kaggle competitions download -c nlp-getting-started
# !pip install voila


# In[5]:


# from zipfile import ZipFile
import pandas as pd 
import string
import re
import os 


# In[6]:


# cwd = "C:\\Users\\Lenovo\\Downloads\\"# Replace with your local pc path
# os.chdir(cwd)
# zip_location = "nlp-getting-started.zip"
# zip = os.path.join(cwd, zip_location)
# path = "kaggle-competition"
# read_data = os.path.join(cwd,path)
# print('Current Working Directory',os.getcwd())
# # data_save = "C:\\Users\\Lenovo\\Downloads"


# In[7]:


# # !mkdir kaggle-competition
# with ZipFile(zip, 'r') as zipObj:
#    # Extract all the contents of zip file in different directory
#    zipObj.extractall('kaggle-competition')


# In[8]:


df = pd.read_csv("data/train.csv")


# In[9]:


df.head()


# In[11]:


# missing_column = (df.isna().sum()/len(df))*100
# print(missing_column)

def missing_column(x):

    dataframe = (df.isna().sum()/len(x))*100
    result = dataframe.head()
    print (result)

missing_column(df)


# In[ ]:





# In[12]:


location = df['location']
id_list = df['id']
keywords = df['keyword']
df = df.drop(['location','id','keyword'],axis=1)
df = df.dropna(axis='rows')
df.head()


# In[13]:


new_df = df.duplicated()
new_df.head()


# In[14]:


df["text"] = df['text'].str.replace('http\S+|www.\S+', '', case=False)
df.head()


# In[16]:


def tokenize(txt):
  tokens=re.split("\W+",txt)# "W+" is represented for non words and "+" represents one or more words
  return tokens

df["text_tokenized"]=df["text"].apply(lambda x:tokenize(x))
df.head()


# In[19]:


def rem_punctate(txt):
  txt_nopunt="".join([ c for c in txt if c not in string.punctuation])
  return txt_nopunt

df['text_clean']= df['text'].apply(lambda x: rem_punctate(x))

df.head()
df.loc[25:27,"text_clean"]


# In[ ]:




