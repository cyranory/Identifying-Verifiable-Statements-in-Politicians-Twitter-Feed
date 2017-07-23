from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from sklearn.externals import joblib

def train_sentiment():
    instances = 8000
    subj = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:instances]]
    obj = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:instances]]
    train_subj = subj
    train_obj = obj
    train_set = train_subj + train_obj
    sentiment = SentimentAnalyzer()
    all_neg = sentiment.all_words([mark_negation(doc) for doc in train_set])
    uni_g = sentiment.unigram_word_feats(all_neg, min_freq=4)
    sentiment.add_feat_extractor(extract_unigram_feats, unigrams=uni_g)
    trained_set = sentiment.apply_features(train_set)
    nb = NaiveBayesClassifier.train
    classifier = sentiment.train(nb, trained_set)
    return classifier

a = train_sentiment()
filename = 'sentiment_analyzer.joblib.pkl'
_ = joblib.dump(a, filename, compress=9)