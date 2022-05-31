import pandas as pd
import matplotlib.pyplot

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from wordcloud import WordCloud
from tqdm import tqdm
from functions_cleaning_5 import *


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


pisupisu = "Lorem 666 ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta; lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-)."

result = clean_up(pisupisu)

print(pisupisu)
print("Oczyszczony tekst\n")
print(result)
print(type(result))
print('\n')
print(stopwords.words('english'))
print('\n')

######

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = stopwords.words('english')

print(example_sent)
print(filtrowanie_tekstu(example_sent))
print('\n')

######

ps = PorterStemmer()

words = ["program", "programs", "programmer", "programming", "programmers"]

for w in words:
    print(w, " : ", ps.stem(w))

sentence = "Programmers program with programming languages"

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

tekst = "Lorem 666 ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta; lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-)."

tekst = text_tokenizer(string)
bow = bag_of_words(tekst)
wordcloud(bow)

vectorizer = CountVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(df['title'])

vectorizer_tfidf = TfidfVectorizer(tokenizer=text_tokenizer)
transform_tfidf = vectorizer_tfidf.fit_transform(df['title'])
print(vectorizer.get_feature_names_out())
print(X_transform.toarray())
print(X_transform)
print(X_transform.shape)
columns = vectorizer_tfidf.get_feature_names_out()
weights = transform_tfidf.toarray().mean(axis=0)

print("Top 10 najczęściej występujące tokeny")
print(top_10_najczesciej_tokeny(X_transform.toarray().sum(axis=0), vectorizer.get_feature_names_out(), 10))

print("Top 10 najważniejszych tokenów")
print(top_10_najczesciej_tokeny(transform_tfidf.toarray().sum(axis=0), vectorizer_tfidf.get_feature_names_out(), 10))

show_plot_most_important(top_10_najczesciej_tokeny(X_transform.toarray().sum(axis=0), vectorizer.get_feature_names_out(), 10),
                    bow, "Tokeny występujące najczęściej wg ilości")

print(prettytable_most_important(top_10_najczesciej_tokeny(X_transform.toarray().sum(axis=0), vectorizer.get_feature_names_out(), 10),
                                 bow, "Tokeny występujące najczęściej wg ilości"))

show_key_plot(columns, weights)

print('Ładne tabelki\n')
print(prettytable_tfidf_key(columns, weights))
