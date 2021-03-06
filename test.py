import numpy as np
from main import TOTAL
from main import GTOTAL

global GTOTAL
global TOTAL

def test1():
    T = input()
    for i in range(eval(T)):
        w1 = input()
        w2 = input()
        if w1 in index and w2 in index:
            print(np.dot(mat[index[w1]],mat[index[w2]])/(np.linalg.norm(mat[index[w1]])*np.linalg.norm(mat[index[w2]])))
        else:
            print("words doesn't exists")

def test2(index, mat, mwords):
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

def test3(index, mat, gwords):
    x = input()
    y = input()
    if not x in index or not y in index:
        print("word do not exists")
        return
    vecx = mat[index[x]]
    vecy = mat[index[y]]
    ax = np.average(vecx)
    ay = np.average(vecy)
    vecm = vecx * vecy
    mm = np.average(vecm)
    a = set()
    print("xword:")
    for i in sorted(enumerate(vecx), key=lambda x:x[1], reverse=1)[0:10]:
        print(i[0],i[1],int(i[0]/GTOTAL),gwords[i[0]%GTOTAL][0])
    print("====================\nyword:")
    for i in sorted(enumerate(vecy), key=lambda x:x[1], reverse=1)[0:10]:
        print(i[0],i[1],int(i[0]/GTOTAL),gwords[i[0]%GTOTAL][0])
    for i in sorted(enumerate(vecx), key=lambda x:x[1], reverse=1)[0:30]:
        a.add(i[0])
    print("====================\nword in commmon:")
    for i in sorted(enumerate(vecy), key=lambda x:x[1], reverse=1)[0:30]:
        if i[0] in a: print(i[0],int(i[0]/GTOTAL),gwords[i[0]%GTOTAL][0])

def test4(gindex, mat, mwords):
    x = input()
    if not x in gindex:
        print("word do not exists")
        return
    y = eval(input())
    idx = gindex[x]
    ls = []
    for i,v in enumerate(mat):
        ls.append((i, v[y*GTOTAL+idx]))
    for i in sorted(ls, key=lambda x:x[1], reverse=1)[0:10]:
        print(mwords[i[0]][0], mat[i[0]][idx+y*GTOTAL])

def test_word_frequency(mwords):
    fre = list(map(lambda x: np.log(x[1]), mwords))
    import matplotlib.pyplot as plt
    plt.bar(range(len(fre)), sorted(fre, reverse = 1))
    plt.show()