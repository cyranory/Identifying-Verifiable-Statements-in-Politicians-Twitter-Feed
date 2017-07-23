import random
# loads the number of data from a file
def load_data(file,num):
    f = open(file, 'r', encoding='utf-8')
    label = []
    statement = []
    test = []
    count = 0
    for line in f:
        if count == num:
            break
        else:
            a = line.split(":")
            label.append(a[0])
            statement.append(a[1].strip().lower())
            count += 1
    f.close()
    return label,statement

def load_data_csv(file):
    f = open(file, 'r', encoding='utf-8')
    label = []
    sentences = []
    for line in f:
        label.append(line[0])
        sentences.append(line[2:].strip())
    f.close()
    t_label = []
    for item in label:
        if item == '0':
            t_label.append('unverifiable')
        elif item == '1':
            t_label.append('verifiable')
        else:
            t_label.append('verifiable')
    return t_label,sentences

#splits data into 7:3
def split_data(list):
    a = len(list)/10
    major = int(a * 7)
    minor = int(a * 3)
    list1 = list[:major]
    list2 = list[-minor:]
    return list1,list2

#combine data
def combine(list1,list2):
    results = list1 + list2
    return results

def shuffle(list1,list2):
    a = list1
    b = list2
    c = list(zip(a, b))
    random.shuffle(c)
    l1,l2 = zip(*c)
    return l1,l2
