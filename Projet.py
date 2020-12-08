from flask import Flask, render_template, redirect, request, url_for, redirect
from flask import Flask
import nltk
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from flask import jsonify


def pre_process(corpus):
    corpus = corpus.lower()
    stopset = stopwords.words('english') + list(string.punctuation)
    corpus = " ".join([i for i in word_tokenize(corpus) if i not in stopset])
    corpus = unidecode(corpus)
    return corpus

model = Word2Vec(sentences=common_texts, window=5, min_count=1, workers=4)
word_emb_model = model

def get_cosine_similarity(feature_vec_1, feature_vec_2):    
    return cosine_similarity(feature_vec_1.reshape(1, -1), feature_vec_2.reshape(1, -1))[0][0]

df = pd.read_csv('tweets.csv')
df.drop_duplicates(subset ="text", keep = False, inplace = True)
#df = df.head(1000)
l = []

#corpus = ['America is terrible right now']

#for c in range(len(corpus)):
 #   corpus[c] = pre_process(corpus[c])


#for i in df['Unnamed: 0']:
 #   l1=[]
  #  df1 = df.loc[lambda df: df['Unnamed: 0'] == i]
   # a = str(df1['text'])
   # l1.append(a)
   # l1[0] = pre_process(l1[0])
   # tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2))
   # tfidf_vectorizer.fit(l1)
   # feature_vectors = tfidf_vectorizer.transform(l1)
   # feature_vectors1 = tfidf_vectorizer.transform(corpus)
   # l.append(get_cosine_similarity(feature_vectors, feature_vectors1))


#l2=[]
#for i in range (0,len(l)):
#    if l[i] !=0:
#        l2.append(i)

#d = {}
#for i in l2:
#    d[i] = l[i]

#d1 = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
#l5=[]
#for i in range(1,20):
 #   df3 = df.loc[lambda df: df['Unnamed: 0'] == list(d1)[-i]]
   # a = str(df3['text'])
    #l5.append(a)
    #l5.append('<br/>')
    #joined_string = "".join(l5)


#str1 = '\n'.join(l5)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("test.html")

@app.route("/text", methods=["POST","GET"])
def text():
    if request.method == "POST":
        corpus = []
        corpus.append(request.form["nm"])
        for c in range(len(corpus)):
            corpus[c] = pre_process(corpus[c])


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


        l2=[]
        for i in range (0,len(l)):
            if l[i] !=0:
                l2.append(i)

        d = {}
        for i in l2:
            d[i] = l[i]

        d1 = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        l5=[]
        for i in range(1,20):
            df3 = df.loc[lambda df: df['Unnamed: 0'] == list(d1)[-i]]
            a = str(df3['text'])
            l5.append(a)
            l5.append('<br/>')
            joined_string = "".join(l5)
          
        return joined_string
          
          

    else:
        return render_template("text.html")

#@app.route("/result")
#def result(yourtext):
    #return {yourtext}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


    