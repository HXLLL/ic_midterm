from data import *
import parse
import numpy as np
import pdb
import test
import pickle

global TOTAL
TOTAL = 1000

def input_parse():
    datafile = 'data2.dat'
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
    #pdb.set_trace()
    for s in sentences:
        S += 1
        if S % 10000 == 0: print(S)
        words = parse.getwords(s)
        for idx,w in enumerate(words):
            if not w in index: continue
            wid = index[w]
            if idx-3 >= 0 and words[idx-3] in index: mat[wid][index[words[idx-3]]] += 0.5
            if idx-2 >= 0 and words[idx-2] in index: mat[wid][index[words[idx-2]]] += 1
            if idx-1 >= 0 and words[idx-1] in index: mat[wid][index[words[idx-1]]] += 2
            if idx+1 < len(words) and words[idx+1] in index: mat[wid][index[words[idx+1]]] += 2
            if idx+2 < len(words) and words[idx+2] in index: mat[wid][index[words[idx+2]]] += 1
            if idx+3 < len(words) and words[idx+3] in index: mat[wid][index[words[idx+3]]] += 0.5
    with open(datafile, "wb") as f:
        pickle.dump((article, sentences, dic, index, mwords, mat),f)


if __name__ == "__main__":
    datafile = 'data2.dat'
    article = ''
    sentences = []
    dic = {}
    index = {}
    mwords = []
    mat = []

    with open(datafile, "rb") as f:
        (article, sentences, dic, index, mwords, mat) = pickle.load(f)

    def pmi():
        for i in range(TOTAL):
            #alpha = 1/np.log(mwords[i][1])
            alpha = 1
            if len(mwords[i][0])<=3 : alpha = 0
            for j in range(TOTAL):
                mat[j][i] *= alpha
    pmi()
    print("words:")
    print(mwords)
#test1
    def test1():
        T = input()
        for i in range(eval(T)):
            w1 = input()
            w2 = input()
            if w1 in index and w2 in index:
                print(np.dot(mat[index[w1]],mat[index[w2]])/(np.linalg.norm(mat[index[w1]])*np.linalg.norm(mat[index[w2]])))
            else:
                print("words doesn't exists")

    def test2():
        T = input()
        for i in range(eval(T)):
            pdb.set_trace()
            w1 = input()
            if w1 in index:
                ls = []
                idx = index[w1]
                for w2 in range(TOTAL):
                    ls.append((w2,np.dot(mat[idx],mat[w2])/np.linalg.norm(mat[idx])/np.linalg.norm(mat[w2])))
                for w in sorted(ls, key=lambda x:x[1],reverse=1)[0:20]:
                    print(mwords[w[0]][0], w[1])
            else:
                print("words doesn't exists")

    test2()