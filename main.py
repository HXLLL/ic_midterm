from data import *
import parse
import numpy as np
import pdb
import test
import pickle
import test
import kmeans

TOTAL = 1000

def input_parse():
    datafile = 'data1.dat'
    article = input_article('article/quora_questions_gbk.txt')
    sentences = parse.getsentences(article)
    print("sentence parsed")
    dic = parse.makedic(article)
    print("dict made")
    index = {}
    mwords = sorted(dic.items(), key=lambda x:x[1], reverse=1)[0:TOTAL]
    for idx,s in enumerate(mwords):
        index[s[0]] = idx

    print("calcaluting mat")
    mat = np.zeros((TOTAL,TOTAL))
    S = 0
    for s in sentences:
        S += 1
        if S % 10000 == 0: print(S)
        words = parse.getwords(s)
        for idx,w in enumerate(words):
            if not w in index: continue
            wid = index[w]
            #if idx-3 >= 0 and words[idx-3] in index: mat[wid][index[words[idx-3]]] += 0.5
            #if idx-2 >= 0 and words[idx-2] in index: mat[wid][index[words[idx-2]]] += 1
            if idx-1 >= 0 and words[idx-1] in index: mat[wid][index[words[idx-1]]] += 1
            if idx+1 < len(words) and words[idx+1] in index: mat[wid][index[words[idx+1]]] += 1
            #if idx+2 < len(words) and words[idx+2] in index: mat[wid][index[words[idx+2]]] += 1
            #if idx+3 < len(words) and words[idx+3] in index: mat[wid][index[words[idx+3]]] += 0.5

    def pmi():
        for i in range(TOTAL):
            alpha = 1.0/np.log(mwords[i%TOTAL][1])**2
            #if len(mwords[i][0])<=3 : alpha = 0
            for j in range(TOTAL):
                mat[j][i] *= alpha
    pmi()

    with open(datafile, "wb") as f:
        pickle.dump((article, sentences, dic, index, mwords, mat),f)


if __name__ == "__main__":
    datafile = 'data1.dat'
    article = ''
    sentences = []
    dic = {}
    index = {}
    mwords = []
    mat = []

    with open(datafile, "rb") as f:
        (article, sentences, dic, index, mwords, mat) = pickle.load(f)

    k = 130
    res = kmeans.kmeans(mat, k)
    with open("result4.txt","w") as f:
        for i in res:
            for j in i:
                f.write("%s " % mwords[j][0])
            f.write("\n\n")