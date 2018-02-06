# clean chapter files & store them in chapter#_cleaned.txt & return list of unique words in document

import numpy as np
import os.path
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


def text_cleaner(filepath, filename):
    '''
    A function to clean/preprocess text files. 
    - Input: text document file name and path (type: .txt file)
    - Output: list of unique words in document (type: list)
    '''
    
    file_to_open = os.path.join(filepath, filename)
    
    # read file
    try:
        text_corpus = open(file_to_open, "r")
    except IOError: 
        print("Error: File does not exist!")
        return 0
    
    # tokenize and lowercase text
    word_list = [word.lower() for line in text_corpus for word in line.split()]
    
    # remove special characters & numbers with regular expressions
    word_reg = []
    for word in word_list:
        w = re.sub('[^A-Za-z]+', '', word)
        word_reg.append(w)
    
    # remove stopwords
    cleaned_tokens = []
    stop_words = set(stopwords.words('english'))
    for token in word_reg:
        if token not in stop_words:
            cleaned_tokens.append(token)
    
    # lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []
    for token in cleaned_tokens:
        lemmatized_tokens.append(lemmatizer.lemmatize(token))
    
    word_list = list(set(lemmatized_tokens))
    
    return word_list


if __name__ == '__main__':
    text_cleaner(filepath, filename)
