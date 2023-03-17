import json
from wordcloud import WordCloud
from stop_words import get_stop_words
from django.conf import settings

def parseJson(rowText:str):
    data = json.load(rowText)
    return(data)

def findMessages(data:any):
    punct = ['.', ',', '!', '?', ')', '(']

    data_string = ''
    for i in data['messages']:
        if i.get('text') is not None:
            if type(i['text']) == str:
                word = i['text'].lower()
                #исключение знаков пунктуации
                for c in punct:
                    word = i['text'].replace(c, '').lower()
                #добавление слова в строку со всей перепиской
                data_string += word + ' '
    return(data_string)

def createWordcloud(data_string:str):
    stopwords = get_stop_words("ru")
    wc = WordCloud(
        background_color='white',
        stopwords=set(stopwords),
        height=1000,
        width=1000,
        max_words=80
    )
    wc.generate(data_string)
    file_name = data_string[:10].replace(' ', '') + '.png'
    wc.to_file(str(settings.MEDIA_ROOT) + '/' + file_name)

    return(file_name)
