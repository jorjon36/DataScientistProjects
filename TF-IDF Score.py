# install textblob library and define functions for TF-IDF
!pip install -U textblob
import math
from textblob import TextBlob as tb

def tf(word, doc):
    lenOfDoc = len(doc.words)
    if lenOfDoc < 1: return 0
    else: return doc.words.count(word) / lenOfDoc

def contains(word, docs):
    return sum(1 for doc in docs if word in doc.words)

def idf(word, docs):
    docsCount = contains(word, docs)
    if docsCount < 1 : return 0
    else: return math.log(len(docs) / docsCount)

def tfidf(word, doc, docs):
    return tf(word,doc) * idf(word, docs)


# Create a collection of documents as textblobs
doc1 = tb(txt)
doc2 = tb(txt2)
doc3 = tb(txt3)
docs = [doc1, doc2, doc3]

# Use TF-IDF to get the three most important words from each document
print('-----------------------------------------------------------')
for i, doc in enumerate(docs):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, doc, docs) for word in doc.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))