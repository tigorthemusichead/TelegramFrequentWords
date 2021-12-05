import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from stop_words import get_stop_words
stopwords = get_stop_words("ru")

data_set = []
with open('result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for i in data['messages']:
        data_set.append(i['text'])
    f.close()

with open('text.txt', 'w') as f:
    for i in data_set:
        if type(i) == str:
            f.write(i.lower())
    f.close()

text = open('text.txt', 'r', encoding='utf-8').read()
wc = WordCloud(
    background_color='white',
    stopwords=set(stopwords),
    height=3000,
    width=2000,
    max_words=1000
)
wc.generate(text)
wc.to_file('word_cloud.png')
