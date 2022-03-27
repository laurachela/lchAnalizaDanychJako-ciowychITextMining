import re
import pandas as pd
import matplotlib.pyplot

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from wordcloud import WordCloud
from tqdm import tqdm


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
    # emotki_string = ' '.join([str(element) for element in emotki])
    # laczenie_tekstow = wynik5 + emotki_string
    # return [laczenie_tekstow, emotki, type(emotki)]

    # tekst + emotki
    for em in emotki:
        wynik5 += " " + em

    return wynik5



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

######

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = stopwords.words('english')


def filtrowanie_tekstu(text: str):
    # text = ' '.join([slowo for slowo in re.split('; |, | ', text.lower()) if slowo not in stop_words])
    # return text
    list_of_words = text.split(" ")
    return [word for word in list_of_words if word not in stop_words]


print(example_sent)
print(filtrowanie_tekstu(example_sent))
print('\n')

######

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


def stemming_tekstu_vol2(text: list) -> list:
    porter = PorterStemmer()
    return [porter.stem(word) for word in text]


print('\n')
print(sentence)
zmienione = stemming_tekstu(sentence)
print(zmienione)



# file = open('Fake.csv', encoding='utf-8')
# csvreader = csv.reader(file)

# header = next(csvreader)
# print(header)

# print(type(csvreader))

# number_of_lines = 3
# for i in range(number_of_lines):
#    row = csvreader.readline()
#    print(row)



df = pd.read_csv(r"C:\Users\laptop\lch-textmining\lchAnalizaDanychJakosciowychITextMining\True.csv")

string = ""
for i in tqdm(range(len(df['title']))):
    string += df['title'].iloc[i] + " "
len(string)


def bag_of_words(words: list) -> dict:
    bow = {}
    for word in words:
        if word not in bow.keys():
            bow[word] = 1
        else:
            bow[word] += 1
    return bow


string = ""
for i in tqdm(range(len(df['title']))):
    string += df['title'].iloc[i] + " "
len(string)


wynikOST = stemming_tekstu_vol2(filtrowanie_tekstu(clean_up(string)))

print(bag_of_words(wynikOST))
bow = bag_of_words(wynikOST)

wc = WordCloud()
wc.generate_from_frequencies(bow)
matplotlib.pyplot.imshow(wc, interpolation='bilinear')
matplotlib.pyplot.axis("off")
matplotlib.pyplot.show()
