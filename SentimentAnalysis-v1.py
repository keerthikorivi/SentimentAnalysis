#__author__ = 'keerthikorvi'
import os
from nltk import RegexpTokenizer, word_tokenize
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import PlaintextCorpusReader, stopwords



def filecount(dir_name):
    return len([f for f in os.listdir(dir_name) if os.path.isfile(f)])

def word_feats(words):
    return dict([(word, True) for word in words])

def removeAllStopWords(TokenizedText):
    english_stops=set(stopwords.words('english'))
    return english_stops

def tokenizeWords(corpus_root):
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    tokenizer = RegexpTokenizer(r'\w+')
    # for fileid in wordlists.fileids():
    #     sentimentText=wordlists.raw(fileid).lower()
    #     tokenizedWords=tokenizer.tokenize(sentimentText)
    #     tokenizedTextWithoutStopWords=removeAllStopWords(tokenizedWords)
    #
    #     print(tokenizedTextWithoutStopWords)
    #     if "positive" in corpus_root:
    #         print("positive documents")
    #         #posfeats.update(word_feats(tokenizedTextWithoutStopWords),'pos')
    #         #posfeats =posfeats+[word_feats(tokenizedTextWithoutStopWords), 'pos']
    #         posfeats[word_feats(tokenizedTextWithoutStopWords)]='pos'
    #
    #     if "negative" in corpus_root:
    #         negfeats.update(word_feats(tokenizedTextWithoutStopWords),'neg')
    if "negative" in corpus_root:
        negfeats = [(word_feats(removeAllStopWords(tokenizer.tokenize(wordlists.raw(f).lower()))), 'neg') for f in wordlists.fileids()]
    if "positive" in corpus_root:
        posfeats = [(word_feats(removeAllStopWords(tokenizer.tokenize(wordlists.raw(f).lower()))), 'pos') for f in wordlists.fileids()]
        print(posfeats)




positive_articles_dir='C:\\Masters\\project-690\\training set\\lexisnexis\\positivedir'
negative_articles_dir='C:\\Masters\\project-690\\training set\\lexisnexis\\negativeArticlesText'

tokenizeWords(positive_articles_dir)

