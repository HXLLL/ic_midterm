def input_article(filename):
    f = open(filename, "r", encoding='gbk')
    content = f.read()
    return content