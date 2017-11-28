
# coding: utf-8

# In[6]:

import nltk
nltk.download()


# In[7]:

from nltk.book import *


# In[14]:

length = len(text2)
fdist = FreqDist(text2)
parts = ['of', 'for', 'to', 'the', 'a']
print(length)
print(fdist)
for i in parts:
    print(i,'counts',fdist[i], fdist.freq(i))

