#подключение библиотек
#для открытия файла result.json
import json
#для формирования картинки
from wordcloud import WordCloud
#чтобы хоть как-то отсеить действительно самые частые слова)
from stop_words import get_stop_words

#функция генерации картинки
def make(json_adr, res_adr):
    #получение стоп слов (которые сразу будут исключены из анализа)
    stopwords = get_stop_words("ru")
    punct = ['.', ',', '!', '?', ')', '(']
    #строка, в которой будет лежать вся переписка
    data_string = ''
    #открытие json файла
    with open(json_adr + 'result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        #перебор всех сообщений
        for i in data['messages']:
            if i.get('text') is not None:
                if type(i['text']) == str:
                    word = i['text'].lower()
                    #исключение знаков пунктуации
                    for c in punct:
                        word = i['text'].replace(c, '').lower()
                    #добавление слова в строку со всей перепиской
                    data_string += word + ' '
        f.close()
    #настройка картинки
    wc = WordCloud(
        #цвет фона (можно менять)
        background_color='white',
        stopwords=set(stopwords),
        #высота картинки (можно менять)
        height=1000,
        #ширина картинки (можно менять)
        width=1000,
        #количество слов на картинке (можно менять, чем больше слов, тем дольше работает программа)
        #python anywhere справляется только с 80ю, компьютер легко обрабатывает больше 1000
        max_words=80
    )
    #генерация картинки
    wc.generate(data_string)
    #сохранение картинки
    wc.to_file(res_adr + 'word_cloud.png')
