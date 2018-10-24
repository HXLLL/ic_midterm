import data
import parse
import numpy as np

global TOTAL
TOTAL = 10

if __name__ == "__main__":
    article = data.input_article('article/1.txt')
    sentences = parse.getsentences(article)
    dic = parse.makedic(article)
    index = {}
    mwords = sorted(dic.items(), key=lambda x:x[1], reverse=1)[0:TOTAL]
    for idx,s in enumerate(mwords):
        index[s[0]] = idx

    mat = np.zero(TOTAL,TOTAL)
    for s in sentences:
        words = parse.getwords(s)
        for idx,w in enumerate(words):
            if not w in index: continue
            wid = index[w]
            if idx-2 >= 0 and words[idx-2] in index: mat[wid][index[words[idx-2]]] += 1
            if idx-1 >= 0 and words[idx-1] in index: mat[wid][index[words[idx-1]]] += 1
            if idx+1 >= 0 and words[idx+1] in index: mat[wid][index[words[idx+1]]] += 1
            if idx+2 >= 0 and words[idx+2] in index: mat[wid][index[words[idx+2]]] += 1

    T = input()
    for i in range(T):
        w1 = input()
        w2 = input()
        if w1 in index and w2 in index:
            print(np.cos(mat[index[w1]],mat[index[w2]]))