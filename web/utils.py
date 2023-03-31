import json
from wordcloud import WordCloud
from stop_words import get_stop_words
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import File
from datetime import datetime, timezone, timedelta

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

def createWordcloud(data_string:str, data:any):
    stopwords = get_stop_words("ru")
    file_name = get_random_string(length=10) + '.png'
    file_path = str(settings.MEDIA_ROOT) + '/' + file_name
    try:
        wc = WordCloud(
            background_color=data['background'],
            stopwords=set(stopwords),
            height=int(data['height']),
            width=int(data['width']),
            max_words=int(data['word_count'])
        )
        wc.generate(data_string)
        wc.to_file(file_path)
    except:
        wc = WordCloud(
            background_color='white',
            stopwords=set(stopwords),
            height=1000,
            width=1000,
            max_words=80
        )
        wc.generate(data_string)
        wc.to_file(file_path)
    record = File(file_name = file_name)
    record.save()
    print((datetime.now(timezone.utc) - record.created_on).total_seconds() > 60)
    return(file_name)

def createMessage(data):
    message = ""
    message += "New message to wordcloud support\n"
    message += "\n"
    message += "Name: " + data['name'] + "\n"
    message += "Contact method: " + data['contactMethod'].lower() + "\n"
    if data['contactMethod'] == "TELEGRAM":
        message += "Telegram user name: " + data['tgUserName'] + "\n"
    else:
        message += "Email: " + data['email'] + "\n"
    message += "\n\n"
    message += data['message']
    
    return message

