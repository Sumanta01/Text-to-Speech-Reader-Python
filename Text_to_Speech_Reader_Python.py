# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 01:51:42 2023

@author: KIIT
"""

from newspaper import Article
import nltk
from gtts import gTTS
import os

article=Article("https://indianexpress.com/todays-paper/")

article.download()
article.parse()

nltk.download('punkt')
article.nlp()

my_text=article.text

language='en' #English


my_obj=gTTS(text=my_text,lang=language,slow=False)

my_obj.save("my_read_article.mp3")

os.system("start my_read_article.mp3")