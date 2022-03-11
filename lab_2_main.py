import re
# import nltk  # Biblioteka NLTK ang. Natural Language Toolkit

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Zadanie 1. (pierwsza część zajęć) funkcja clean_up


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
    cousunac4 = '[,;:\.]|'
    wynik4 = re.sub(cousunac4, '', wynik3, count=0, flags=0)
    # convert letters to their lowercase version
    small = wynik4.lower()
    # usunąć nadmiarowe spacje
    cousunac5 = ' {2,}'  # lub '[]{2,}' lub ' +' -> od jednej spacji
    wynik5 = re.sub(cousunac5, '', small, count=0, flags=0)
    # sklejanie tekstów (tekst z emotek i tekst wyjściowy)
    emotki_string = ' '.join([str(element) for element in emotki])
    laczenie_tekstow = wynik5 + emotki_string

    return [laczenie_tekstow, emotki, type(emotki)]


pisupisu = "Lorem 666 ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta; lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-)."

result = clean_up(pisupisu)

print(pisupisu)
print("Oczyszczony tekst\n")
print(result)
print(type(result))
# ['abc', 100]
# <class 'list'>

print('\n')
print(stopwords.words('english'))
print('\n')

# Zadanie 2. (pierwsza część zajęć) stop_words
# nltk.download('stopwords') # -> pip install nltk
example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = stopwords.words('english')


def filtrowanie_tekstu(text: str):
    text = ' '.join([slowo for slowo in re.split('; |, | ', text.lower()) if slowo not in stop_words])
    return text


print(example_sent)
print(filtrowanie_tekstu(example_sent))
print('\n')


# Zadanie 1. (druga część zajęć)
# Funkcja, która jako parametr przyjmuje tekst (:str), a zwraca listę (→list) wyrazów poddanych procesowi stemmingu
# z wykorzystaniem biblioteki nltk , proces ten ma bazować na algorytmie Portera.

ps = PorterStemmer()

words = ["program", "programs", "programmer", "programming", "programmers"]

for w in words:
    print(w, " : ", ps.stem(w))

sentence = "Programmers program with programming languages"


def stemming_tekstu(text: str) -> list:
    lista_slow = []
    for word2 in [slowo for slowo in re.split('; |, | ', text.lower())]:
        lista_slow.append(ps.stem(word2))

    return lista_slow


print('\n')
print(sentence)
print(stemming_tekstu(sentence))
