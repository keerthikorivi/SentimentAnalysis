# #__author__ = 'keerthikorvi'
# import csv
# import logging
# import nltk
# import re
# from nltk.corpus import sentiwordnet  as swn,webtext,gutenberg,nps_chat,brown,udhr,wordnet,PlaintextCorpusReader,SentiWordNetCorpusReader
# from nltk.tokenize import WordPunctTokenizer,LineTokenizer,word_tokenize, RegexpTokenizer
# from nltk import sent_tokenize
# from nltk.corpus import stopwords
# import enchant
# from nltk.metrics import edit_distance
#
# dictionaryOfWordsWithSentiment={}
# replacement_patterns = [
#   (r'won\'t', 'will not'),
#   (r'can\'t', 'cannot'),
#   (r'i\'m', 'i am'),
#   (r'ain\'t', 'is not'),
#   (r'(\w+)\'ll', '\g<1> will'),
#   (r'(\w+)n\'t', '\g<1> not'),
#   (r'(\w+)\'ve', '\g<1> have'),
#   (r'(\w+)\'s', '\g<1> is'),
#   (r'(\w+)\'re', '\g<1> are'),
#   (r'(\w+)\'d', '\g<1> would')
# ]
#
# class RegexpReplacer(object):
#   def __init__(self, patterns=replacement_patterns):
#     self.patterns = [(re.compile(regex), repl) for (regex, repl) in
#       patterns]
#
#   def replace(self, text):
#     s = text
#     for (pattern, repl) in self.patterns:
#       s = re.sub(pattern, repl, s)
#     return s
#
# #spelling correction with dictionary words.
#
# class SpellingReplacer(object):
#   def __init__(self, dict_name='en', max_dist=2):
#     self.spell_dict = enchant.Dict(dict_name)
#     self.max_dist = max_dist
#
#   def replace(self, word):
#     if self.spell_dict.check(word):
#       return word
#     suggestions = self.spell_dict.suggest(word)
#
#     if suggestions and edit_distance(word, suggestions[0]) <=self.max_dist:
#       return suggestions[0]
#     else:
#       return word
#
#
# #nltk.download()
# #text1.concordance("monstrous")
# #text1.similar("monstrous")
# #for fileid in webtext.fileids():
#     #print(fileid, webtext.raw(fileid)[:65], '...')
# #for fileid in gutenberg.fileids():
#    # print(fileid, gutenberg.raw(fileid))
#
#
# def cleanData(articleText):
#     articleText=articleText.lower()
#
# def removeAllStopWords(TokenizedText):
#     english_stops=set(stopwords.words('english'))
#     '''
#     english_stops.add('$')
#     english_stops.add('--')
#     english_stops.add("''")
#     english_stops.add('?')
#     english_stops.add(',')
#     english_stops.add('-')
#     english_stops.add('.')
#     english_stops.add(';')
#     english_stops.add(':')
#     '''
#
#     WordListWithStopWordsRemoved=[word for word in  TokenizedText if word not in english_stops]
#     #WordListWithStopWordsRemoved = [x for x in WordListWithStopWordsRemoved if not isinstance(x, int)]
#     WordListWithStopWordsRemoved = [x for x in WordListWithStopWordsRemoved if not (x.isdigit())]
#     #print(WordListWithStopWordsRemoved)
#
# def readcsv():
#     f = open('polarity.csv')
#     csv_f = csv.reader(f,delimiter=" ")
#     i=0
#     for row in csv_f:
#             # send the browser,ticker,date and company name details to download the documents
#             logging.debug('current request'+row[0]+":"+row[1]+":"+row[2]+":"+row[3]+":"+row[4]+":"+row[5])
#             print('current request'+row[0]+":"+row[1]+":"+row[2]+":"+row[3]+":"+row[4]+":"+row[5])
#             splitWord=str(row[2]).split("=")
#             splitPolarity=str(row[5]).split("=")
#             print(splitWord)
#             print(splitPolarity)
#             try:
#              print('hey')
#             except BaseException as e:
#                 logging.info('ERROR:SEARCH FAILED')
#
#     f.close()
#
# readcsv()
# corpus_root='C:\\Masters\\project-690\\lexisnexiscorpora'
# wordlists = PlaintextCorpusReader(corpus_root, '.*')
# #tokenizer=WordPunctTokenizer()
# tokenizer = RegexpTokenizer(r'\w+')
# for fileid in wordlists.fileids():
#     #print(fileid, wordlists.raw(fileid))
#     #print(fileid)
#     #if('cv000_29416.txt'==fileid):
#         #print(fileid, wordlists.raw(fileid))
#     lengthOfDocument=wordlists.raw(fileid)
#     #print('length of document'+str(lengthOfDocument))
#     #print(tokenizer.tokenize(wordlists.raw(fileid)))
#     #print(sent_tokenize(wordlists.raw(fileid)))
#     sentimentText=wordlists.raw(fileid).lower()
#     replacer = RegexpReplacer()
#     sentimentText=replacer.replace(sentimentText)
#     tokenizedWords=tokenizer.tokenize(sentimentText)
#     tokenizedTextWithoutStopWords=removeAllStopWords(tokenizedWords)
#     TokenizedWordsWithPosTagger=nltk.pos_tag(sentimentText)
#     text = word_tokenize(sentimentText)
#     TokenizedWordsWithPosTagger=nltk.pos_tag(text)
#     removeStopWords= [x for x in TokenizedWordsWithPosTagger if x[1]!="DT" and x[1]!=":"]
#     #print(removeStopWords)
#
#
#
#
#
# def calculatePolarityOfTheDocument(tokenizedTextAfterCleaning):
#     pass
#
