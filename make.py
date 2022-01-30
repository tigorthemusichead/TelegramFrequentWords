import json
from wordcloud import WordCloud
from stop_words import get_stop_words


def make(json_adr, res_adr):
    stopwords = get_stop_words("ru")
    punct = ['.', ',', '!', '?', ')', '(']
    data_string = ''
    with open(json_adr, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data['messages']:
            if type(i['text']) == str:
                for c in punct:
                    word = i['text'].replace(c, '').lower()
                    data_string += word + ' '
        f.close()

    wc = WordCloud(
        background_color='white',
        stopwords=set(stopwords),
        height=500,
        width=500,
        max_words=1000
    )
    wc.generate(data_string)
    wc.to_file(res_adr + 'word_cloud.png')

