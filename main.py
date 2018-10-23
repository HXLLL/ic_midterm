import data
import pase
if __name__ == "__main__":
    article = data.input_article('article/1.txt')
    sentences = parse.getsentences(article)
    dic = parse.makedic(article)