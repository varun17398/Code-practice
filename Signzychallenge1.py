#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


df=pd.read_csv('C:\\Users\\rakesh.bachu\\Desktop\\Long Forms\\Signzy challenge\\labeledTrainData.tsv',header=0,delimiter='\t')


# In[11]:


df


# In[12]:


from nltk.corpus import stopwords


# In[13]:


from bs4 import BeautifulSoup
import nltk
import os


# In[14]:


from textblob import TextBlob
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.corpus import stopwords


# In[15]:


sw=stopwords.words("english")


# In[16]:


reviews=[]
for i in range(0,len(df['review'])):
    reviews.append(df['review'][i].lower())


# In[17]:


reviews


# In[18]:


import re


# In[19]:


def clean_review(text):
    let=re.sub("[^a-zA-Z]", " ",text)
    words = let.split()
    finalwords=[w for w in words if not w in sw]
    return(" ".join(finalwords))


# In[22]:


cleanreviews=[]
n=len(reviews)
for i in range(0,n):
    cleanreviews.append(clean_review(reviews[i]))


# In[23]:


cleanreviews


# In[24]:


from sklearn.feature_extraction.text import CountVectorizer


# In[25]:


vectorizer = CountVectorizer(analyzer = "word",                                tokenizer = None,                                 preprocessor = None,                              stop_words = None,                                max_features = 5000) 
train_data_features = vectorizer.fit_transform(cleanreviews)
train_data_features = train_data_features.toarray()


# In[26]:


from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 150) 
forest = forest.fit( train_data_features, df["sentiment"] )


# In[27]:


df1=pd.read_csv('C:\\Users\\rakesh.bachu\\Desktop\\Long Forms\\Signzy challenge\\testData.tsv',header=0,delimiter='\t')


# In[28]:


cleantest=[]
n1=len(df1['review'])
for i in range(0,n1):
    cleantest.append(clean_review(df1['review'][i]))


# In[29]:


test_data_features = vectorizer.transform(cleantest)
test_data_features = test_data_features.toarray()


# In[30]:


final = forest.predict(test_data_features)
df2 = pd.DataFrame( data={"id":df1["id"], "sentiment":final} )


# In[32]:


df2.to_csv( "C:\\Users\\rakesh.bachu\\Desktop\\submission.csv", index=False)


# In[ ]:




