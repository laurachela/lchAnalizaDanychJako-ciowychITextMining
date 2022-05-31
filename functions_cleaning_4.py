import re
import numpy as np
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from wordcloud import WordCloud


def clean_up(tekst: str):  # -> str
    x = tekst
    # wyciąganie emotek do listy
    emotki = re.findall('[:;]-?[)(><]', x)
    # usuwanie liczb
    cousunac1 = '[0-9]'
    wynik1 = re.sub(cousunac1, '', x, count=0, flags=0)
    # usuwanie znaczników html
    cousunac2 = '(<([^>]+)>.*?)'
    wynik2 = re.sub(cousunac2, '', wynik1, count=0, flags=0)
    # usuwanie emotek
    cousunac3 = '([:;]-?[)(><])'
    wynik3 = re.sub(cousunac3, '', wynik2, count=0, flags=0)
    # usuwanie znaków interpunkcyjnych
    cousunac4 = '[,;:\n.?!-@]|'
    wynik4 = re.sub(cousunac4, '', wynik3, count=0, flags=0)
    # convert letters to their lowercase version
    small = wynik4.lower()
    # usunąć nadmiarowe spacje
    cousunac5 = ' {2,}'  # lub '[]{2,}' lub ' +' -> od jednej spacji
    wynik5 = re.sub(cousunac5, '', small, count=0, flags=0)
    # sklejanie tekstów (tekst z emotek i tekst wyjściowy)
    # emotki_string = ' '.join([str(element) for element in emotki])
    # laczenie_tekstow = wynik5 + emotki_string
    # return [laczenie_tekstow, emotki, type(emotki)]
    # wynik6_pattern = re.compile(pattern="["
    #                                    u"\U0001F600-\U0001F64F"  # emoticons
    #                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    #                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    #                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    #                                    "]+", flags=re.UNICODE)
    # wynik6=wynik6_pattern.sub(r'', wynik5)

    # tekst + emotki
    for em in emotki:
        wynik5 += " " + em

    return wynik5


def filtrowanie_tekstu(text: str) -> list:
    # text = ' '.join([slowo for slowo in re.split('; |, | ', text.lower()) if slowo not in stop_words])
    # return text
    stop_words = stopwords.words('english')
    list_of_words = text.split(" ")
    return [word for word in list_of_words if word not in stop_words]


def stemming_tekstu(text: str) -> list:
    ps = PorterStemmer()
    lista_slow = []
    for word2 in [slowo for slowo in re.split('; |, | ', text.lower())]:
        lista_slow.append(ps.stem(word2))
    return lista_slow


def stemming_tekstu_vol2(text: list) -> list:
    porter = PorterStemmer()
    return [porter.stem(word) for word in text]


def okreslone_wyrazy(text: list) -> list:
    lista_slow = []
    for word in [slowo for slowo in text]:
        if len(word) > 3:
            lista_slow.append(word)
    return lista_slow


def bag_of_words(words: list) -> dict:
    bow = {}
    for word in words:
        if word not in bow.keys():
            bow[word] = 1
        else:
            bow[word] += 1
    return bow


def wordcloud(bow):
    wc = WordCloud()
    wc.generate_from_frequencies(bow)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def text_tokenizer(text: str) -> list:
    text = clean_up(text)
    text = filtrowanie_tekstu(text)
    text = stemming_tekstu_vol2(text)
    text = okreslone_wyrazy(text)
    return text


def top_10_najczesciej_tokeny(lista_tokeny: list, lista_slowa: list, ilosc: int = 10) -> list:
    lista = lista_tokeny.copy()
    result = []
    for i in range(ilosc):
        tokeny_index = np.argmax(lista)
        result.append(lista_slowa[tokeny_index])
        lista[tokeny_index] = 0
    return result
