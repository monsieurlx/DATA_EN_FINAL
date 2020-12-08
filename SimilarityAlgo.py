#!/usr/bin/env python
# coding: utf-8

# In[128]:


import nltk
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import string
def pre_process(corpus):
    # convert input corpus to lower case.
    corpus = corpus.lower()
    # collecting a list of stop words from nltk and punctuation form
    # string class and create single array.
    stopset = stopwords.words('english') + list(string.punctuation)
    # remove stop words and punctuations from string.
    # word_tokenize is used to tokenize the input corpus in word tokens.
    corpus = " ".join([i for i in word_tokenize(corpus) if i not in stopset])
    # remove non-ascii characters
    corpus = unidecode(corpus)
    return corpus


# In[129]:


from sklearn.feature_extraction.text import TfidfVectorizer



# In[130]:


from gensim.test.utils import common_texts
from gensim.models import Word2Vec
model = Word2Vec(sentences=common_texts, window=5, min_count=1, workers=4)


# In[131]:


from gensim.models import Word2Vec
import numpy as np
word_emb_model = model


# In[132]:





# In[133]:


from sklearn.metrics.pairwise import cosine_similarity
def get_cosine_similarity(feature_vec_1, feature_vec_2):    
    return cosine_similarity(feature_vec_1.reshape(1, -1), feature_vec_2.reshape(1, -1))[0][0]


# In[134]:





# In[135]:


import pandas as pd
df = pd.read_csv('tweets.csv')
df.drop_duplicates(subset ="text", keep = False, inplace = True)


# In[136]:


#On va calculer la similarity avec tous les tweet du dataset 
#On va les insérer dans une liste (par id ou index pour les retrouver )
#On va trier la liste (algo de tri)
#On va prendre les 20 valeurs les plus élevées 


# In[137]:


from sklearn.feature_extraction.text import TfidfVectorizer
#Calculons la similarité d'un string avec tous les tweet 
l = []

corpus = ['America is terrible right now']

for c in range(len(corpus)):
    corpus[c] = pre_process(corpus[c])

#for c in range(len(corpus2)):
    #corpus2[c] = pre_process(corpus2[c])
    
#tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2))
#tfidf_vectorizer.fit(corpus)
#feature_vectors1 = tfidf_vectorizer.transform(corpus)



for i in df['Unnamed: 0']:
    l1=[]
    df1 = df.loc[lambda df: df['Unnamed: 0'] == i]
    a = str(df1['text'])
    l1.append(a)
    l1[0] = pre_process(l1[0])
    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf_vectorizer.fit(l1)
    feature_vectors = tfidf_vectorizer.transform(l1)
    feature_vectors1 = tfidf_vectorizer.transform(corpus)
    l.append(get_cosine_similarity(feature_vectors, feature_vectors1))


# In[138]:


l2=[]
for i in range (0,len(l)):
    if l[i] !=0:
        l2.append(i)


# In[139]:


d = {}
for i in l2:
    d[i] = l[i]


# In[140]:


d1 = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}


# In[141]:


for i in range(1,20):
    df3 = df.loc[lambda df: df['Unnamed: 0'] == list(d1)[-i]]
    a = str(df3['text']+df3['date'])
    print(a)

