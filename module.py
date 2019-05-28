#libraries to be used
import re
import string
import nltk
import time
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize


 
start=time.time() 
lemmatizer = WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')

 
def clean_text(text):
    """
        Remove punctuation and stopwords, lemmatize the text, tokenize the sentence into tokens
    """    
    #text = text.replace("\n", " ")
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = " ".join([lemmatizer.lemmatize(word) for word in tokens if word not in stopwords])
    return text
 
 
def senti_polarity(text):
    """
    Return a sentiment polarity: 0 = negative, 1 = positive
    """
 
    sentiment = 0.0
    tokens_count = 0
 
    text = clean_text(text)
    print(text)
    
    token_word = word_tokenize(text)
    
    wrd_list = []
    for word in token_word : 
        wrd_list.append(word)
        #print(wrd_list)
        
        for x in range(len(wrd_list)):
            for wd in wrd_list:
                synsets = wn.synsets(wd)
                if not synsets:
                    continue
 
            
                synset = synsets[0]
                swn_synset = swn.senti_synset(synset.name())
                sentiment += swn_synset.pos_score() - swn_synset.neg_score()
                tokens_count += 1
                #print(sentiment)
 
    
    if not tokens_count:
        print("No tokens")
       
    f = open("negative-words.txt", "r")
    words2=f.read() 
    for wrd in wrd_list:
        #print(wrd)
        if wrd in words2:
            print(wrd)
            return -1
    
    # sum greater than 0 => positive sentiment
    if sentiment >= 0:
        return 1
    
 
    # negative sentiment
    else:
        return -1
    
end=time.time()
print(senti_polarity("A person is and bleeding"))
print("Time-Taken:",end-start)