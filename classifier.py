from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_selection import SelectKBest,chi2
from sklearn import metrics
from Tokenizer import *
from data_prep import *
from crawler import *
import time

# get tweets from politician
while True:
    try:
        politician = str(input('Please enter politician twitter username' +"\n"))
        start_time = time.time()
        twitter_data = get_twitter_user(politician)
        break
    except Exception as e:
        print('Invalid username, please enter a valid username' + '\n')
print('twitter data ready')

# rl,real = load_data_csv('trump.csv')

# prep verifiable data
v_label,v_data =load_data('verifiable.txt',8500)
# v_d7,v_d3 = split_data(v_data)
# v_l7,v_l3 = split_data(v_label)

# prep unverifiable data
uv_label,uv_data =load_data('unverifiable.txt',8500)
# uv_d7,uv_d3 = split_data(uv_data)
# uv_l7,uv_l3 = split_data(uv_label)

#combine data
# train_data = combine(v_d7,uv_d7)
# train_label = combine(v_l7,uv_l7)
# test_data = combine(v_d3,uv_d3)
# test_label = combine(v_l3,uv_l3)
data = combine(v_data,uv_data)
# t_data = combine(data,real)
label = combine(v_label,uv_label)
# t_label = combine(label,rl)
print('data and labels combined')


#shuffle data
# s_train,y_train = shuffle(train_data,train_label)
# s_test,y_test = shuffle(test_data,test_label)

#get scores
print('getting feature scores')
x_train = get_feature_scores(data)
print('getting twitter feature scores')
x_test = get_feature_scores(twitter_data)
# x_new = SelectKBest(chi2,k=int(len(x_train[0])/3)).fit_transform(x_train,t_label)
# train = x_new[:17000]
nb = MultinomialNB().fit(x_train, label)
print('MultinomialNB training complete')
nb_proba = nb.predict_proba(x_test)
nb_results = nb.predict(x_test)
print('compiling scores')
a = output_scores(nb_results,twitter_data,nb_proba)
print('Output:' ,end="\n")
print_output(a)
# print(metrics.classification_report(rl, nb_results))
print("Overall runtime: %s seconds" % (time.time() - start_time))
