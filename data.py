def input_article(filename):
    f = open(filename, "r", encoding='utf-8')
    content = f.read()
    return content