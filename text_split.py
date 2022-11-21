# Text correct and spliter. 
#https://pypi.org/project/textblob/ refrenced
from textblob import * 


text = "Python is a high-level, general-purpose programming language."

longer_text = '''Beautiful is better than ugly. 
                Explicit is better than implicit. 
                Simple is better than complex. '''


def sentence_split(text):
    sentence = TextBlob(text)
    
    return sentence.sentences

x = sentence_split(longer_text)
print(x[1])


def text_correcter(text):
    return TextBlob(text).correct()