from data import *
import parse
import numpy as np
import pdb
import test
import pickle

global TOTAL
TOTAL = 1000

def input_parse():
    datafile = 'data3.dat'
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
    mat = np.zeros((TOTAL,4*TOTAL))
    S = 0
    #pdb.set_trace()
    for s in sentences:
        S += 1
        if S % 10000 == 0: print(S)
        words = parse.getwords(s)
        for idx,w in enumerate(words):
            if not w in index: continue
            wid = index[w]
            #if idx-3 >= 0 and words[idx-3] in index: mat[wid][index[words[idx-3]]] += 0.5
            if idx-2 >= 0 and words[idx-2] in index: mat[wid][index[words[idx-2]]] += 1
            if idx-1 >= 0 and words[idx-1] in index: mat[wid][TOTAL+index[words[idx-1]]] += 1
            if idx+1 < len(words) and words[idx+1] in index: mat[wid][2*TOTAL+index[words[idx+1]]] += 1
            if idx+2 < len(words) and words[idx+2] in index: mat[wid][3*TOTAL+index[words[idx+2]]] += 1
            #if idx+3 < len(words) and words[idx+3] in index: mat[wid][index[words[idx+3]]] += 0.5
    with open(datafile, "wb") as f:
        pickle.dump((article, sentences, dic, index, mwords, mat),f)


if __name__ == "__main__":
    datafile = 'data3.dat'
    article = ''
    sentences = []
    dic = {}
    index = {}
    mwords = []
    mat = []

    with open(datafile, "rb") as f:
        (article, sentences, dic, index, mwords, mat) = pickle.load(f)

    def pmi():
        for i in range(4*TOTAL):
            alpha = 1.0/np.log(mwords[i%TOTAL][1])**3
            #alpha = 1
            #if len(mwords[i][0])<=3 : alpha = 0
            for j in range(TOTAL):
                mat[j][i] *= alpha
    pmi()
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
        #T = input()
        while True:
            #pdb.set_trace()
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

    #test2()

    pdb.set_trace()
    def test3():
        vecx = mat[index['happy']]
        vecy = mat[index['friend']]
        ax = np.average(vecx)
        ay = np.average(vecy)
        vecm = vecx * vecy
        mm = np.average(vecm)
        a = set()
        print("xword:")
        for i in sorted(enumerate(vecx), key=lambda x:x[1], reverse=1)[0:10]:
            print(i[0],i[1],int(i[0]/1000),mwords[i[0]%1000][0])
        print("====================\nyword:")
        for i in sorted(enumerate(vecy), key=lambda x:x[1], reverse=1)[0:10]:
            print(i[0],i[1],int(i[0]/1000),mwords[i[0]%1000][0])
        for i in sorted(enumerate(vecx), key=lambda x:x[1], reverse=1)[0:30]:
            a.add(i[0])
        print("====================\nword in commmon:")
        for i in sorted(enumerate(vecy), key=lambda x:x[1], reverse=1)[0:30]:
            if i[0] in a: print(i[0],int(i[0]/1000),mwords[i[0]%1000][0])
    test3()