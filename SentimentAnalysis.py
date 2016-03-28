#__author__ = 'keerthikorvi'
import os,math
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
    wordListWithStopWordsRemoved=[word for word in  TokenizedText if word not in english_stops]
    return wordListWithStopWordsRemoved


positive_articles_dir='C:\\Masters\\project-690\\training set\\lexisnexis\\positiveArticlesText'
negative_articles_dir='C:\\Masters\\project-690\\training set\\lexisnexis\\negativeArticlesText'
wordlists_positive = PlaintextCorpusReader(positive_articles_dir, '.*')
wordlists_negative = PlaintextCorpusReader(negative_articles_dir, '.*')
tokenizer = RegexpTokenizer(r'\w+')
negfeats = [(word_feats(removeAllStopWords(tokenizer.tokenize(wordlists_positive.raw(f).lower()))), 'neg') for f in wordlists_positive.fileids()]
print(negfeats)
print('############')
print(len(negfeats)*3/4)
posfeats = [(word_feats(removeAllStopWords(tokenizer.tokenize(wordlists_negative.raw(f).lower()))), 'pos') for f in wordlists_negative.fileids()]
print('############')
print(len(posfeats)*3/4)
print(posfeats)
negcutoff = math.ceil(len(negfeats)*3/4)
poscutoff = math.ceil(len(posfeats)*3/4)
print(negcutoff)
print('*******')
print(poscutoff)
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
outputFile = open('AccuracyFeatures.txt', 'w+')
print('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))
classifier = NaiveBayesClassifier.train(trainfeats)
outputFile.write('accuracy:')
outputFile.write(nltk.classify.util.accuracy(classifier, testfeats))
classifier.show_most_informative_features()
print('done')

