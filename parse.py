import re

def getsentences(content):
    return re.split(r'\s*(?:[\.!\?\n]\s*)+', content)

def makedic(content):
    dic = {}
    words = re.findall(r'\b\w+\b', content)
    for i in words:
        if i in dic: dic[i]=dic[i]+1
        else: dic[i] = 1
    return dic

if __name__ == '__main__':
    import data
    content = data.input_article('article/1.txt')
    print(makedic(content))