#!pip3 install psycopg2-binary
#!pip3 install nltk
#!pip3 install scikit-learn
#!pip3 install pandas
#!pip3 install gensim

import time
import psycopg2
import nltk
import pandas as pd
from logic import globals
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from gensim import corpora
from gensim.models import TfidfModel
from gensim.similarities import MatrixSimilarity

wnl = WordNetLemmatizer ()
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

'''Take in a list of docs and output a pre-processed list of clean docs'''

#preprocess string into clean string
def preprocess_string(string):
    clean_string = ""
    total_words = len(string.split())
    word_count = 0
    for word in string.split():
        word_count += 1
        if word.isalpha() and word not in stop_words:
            lemmit_word = wnl.lemmatize(word)
            stem_word = ps.stem(lemmit_word)
            if word_count < total_words:
                clean_string += stem_word + " "
            else:
                clean_string += stem_word
    return(clean_string)

'''from a list of docs, create a bag of words'''

#tokenize each document in a list of documents
def preprocess_tokens(tokens):
    token_list = []
    for word in tokens:
        if word.isalpha() and word not in stop_words:
            lemmit_word = wnl.lemmatize(word)
            stem_word = ps.stem(lemmit_word)
            token_list.append(stem_word)
    return(token_list)

def list_tokens(list_of_strings):
    list_of_tokens = []
    for string in list_of_strings:
        tokens = word_tokenize(string.lower())
        token_list = preprocess_tokens(tokens)
        list_of_tokens.append(token_list)
    return(list_of_tokens)

def list_matches(list_of_strings, ranks):
    list_of_ranks = []
    count = -1
    for txt, score in zip(list_of_strings, ranks):
        count += 1
        if score >= .5:
            my_tuple = (count, txt, score)
            list_of_ranks.append(my_tuple)
    return(list_of_ranks)

#for a given query, get related-product recommendations
def get_query_results(query, products_dict):
    start_time = time.perf_counter()
    print('\n Running query...')
    products_list = globals.list_dict_values(products_dict)
    product_tokens = list_tokens(products_list)
    term_dict = corpora.Dictionary(product_tokens)
    corpus_bow = [term_dict.doc2bow(doc, allow_update=True) for doc in product_tokens]
    tfidf = TfidfModel(corpus_bow, dictionary = term_dict)
    query_processed = preprocess_string(query)
    query_bow = term_dict.doc2bow(list(query_processed.split()))
    cosine_model = MatrixSimilarity(tfidf[corpus_bow])
    ranks = cosine_model[tfidf[query_bow]]
    list_of_ranks = list_matches(products_list, ranks)
    end_time = time.perf_counter()
    total_time = globals.print_total_time_seconds(start_time, end_time)
    #total_time = print_total_time_seconds(start_time, end_time)
    print('\n Query complete in {}\n'.format(total_time))
    return(list_of_ranks)

#format recommendations for console display
def format_results(list_of_ranks, products_dict):
    print('\n Formatting...\n')
    columns = ['NIPG_CODE', 'NIGP_DESC', 'RANK']
    df = pd.DataFrame(columns = columns)
    for i in list_of_ranks:
        val = i[1]
        score = i[2]
        for k, v in products_dict.items():
            if v == val:
                code = int(k)
                temp_dict = {'NIPG_CODE': int(k), 'NIGP_DESC': val, 'RANK': score}
                temp_df = pd.DataFrame([temp_dict],columns = columns)
                df = pd.concat([df, temp_df], ignore_index = True)
    df = df.sort_values(by = 'RANK', ascending = False)
    df = df.drop('RANK', axis = 1)
    results_str = df.to_string(index=False)
    return(results_str)