import data
import parse
import numpy

if __name__ == "__main__":
    article = data.input_article('article/1.txt')
    sentences = parse.getsentences(article)
    dic = parse.makedic(article)
    index = {}
    mwords = sorted(dic.items(), key=lambda x:x[1], reverse=1)[0:3000]
    for idx,s in enumerate(mwords):
        index[s[0]] = idx

    for s in sentences:
        words = parse.getwords(s)
        for idx,w in enumerate(words):
            pass