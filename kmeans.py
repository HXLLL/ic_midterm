import numpy as np
import pdb

global TOTAL

def calcenter(mat, div, k, n, m):
    cnt = [0 for i in range(k)]
    center = np.zeros(m)
    res = [np.zeros(m) for i in range(k)]
    for i,v in enumerate(mat):
        center += v
        res[div[i]] += v
        cnt[div[i]] += 1
    center /= n
    for i in range(k):
        if cnt[i]!=0: res[i] /= cnt[i]
        else: res[i] = center
    return res

def caldiv(mat, c, k):
    res = [0 for i in range(mat.shape[0])]
    for i,v in enumerate(mat):
        dis = list(map(lambda x:np.linalg.norm(x-v), c))
        res[i] = dis.index(min(dis))
    return res

def delta(mat, c, div, k):
    res = 0
    for i,v in enumerate(mat):
        res += np.linalg.norm(v-c[div[i]])
    return res/mat.shape[0]

def diff(v1,v2):
    cnt = 0
    for i,v in enumerate(v1):
        if v != v2[i]: cnt += 1
    return cnt

def kmeans(mat, k):
    n = mat.shape[0]
    m = mat.shape[1]
    for i in range(n):
        mat[i] = mat[i]/np.linalg.norm(mat[i])
    div = [0 for i in range(n)]
    for i in range(n):
        div[i] = np.random.randint(k)
    c = calcenter(mat, div, k, n, m)
    div = caldiv(mat, c, k)
    epoch = 1000
    for i in range(epoch):
        print("iteration %d, delta:%.16f" % (i, delta(mat, c, div, k)))
        c = calcenter(mat, div, k, n, m)
        prediv = div
        div = caldiv(mat, c, k)
        changes = diff(div, prediv)
        print("%d changes" % changes)
        if changes == 0: break

    res = [[] for i in range(k)]
    for i in range(n):
        res[div[i]].append(i)
    return res

if __name__ == "__main__":
    print(kmeans(np.array([[1.0,2],[3,4]]),1))