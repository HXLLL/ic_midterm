import numpy as np
import pdb

def calcenter(mat, div, k, n, m):
    cnt = [0 for i in range(k)]
    res = [np.zeros(m) for i in range(k)]
    for i,v in enumerate(mat):
        res[div[i]] += v
        cnt[div[i]] += 1
    for i in range(k):
        if cnt[i]!=0: res[i] /= cnt[i]
        else:
            for j in range(m):
                res[i][j] = np.random.random()
    return res

def caldiv(mat, c, k):
    res = [0 for i in range(mat.shape[0])]
    for i,v in enumerate(mat):
        dis = list(map(lambda x:np.linalg.norm(x-v), c))
        res[i] = dis.index(min(dis))
    return res

#def delta(mat, c, div, k):
#    cnt = [0 for i in range(k)]
#    res = [0 for i in range(k)]
#    for i,v in enumerate(mat):
#        res[div[i]] += 
#        cnt[div[i]] += 1
#    for i in range(k):
#        if cnt[i]!=0: res[i] /= cnt[i]
#
#

def kmeans(mat, k):
    n = mat.shape[0]
    m = mat.shape[1]
    for i in range(n):
        mat[i] = mat[i]/np.linalg.norm(mat[i])
    div = [0 for i in range(n)]
    c = calcenter(mat, div, k, n, m)
    div = caldiv(mat, c, k)
    epoch = 20
    for i in range(epoch):
        c = calcenter(mat, div, k, n, m)
        div = caldiv(mat, c, k)

    res = [[] for i in range(k)]
    for i in range(n):
        res[div[i]].append(i)
    return res

if __name__ == "__main__":
    print(kmeans(np.array([[1.0,2],[3,4]]),1))