from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix
from sklearn.preprocessing import normalize
from functions_cleaning import *

df = pd.read_csv('alexa_reviews.csv', sep=";", encoding='cp1252')
df["rating"] = df["rating"].apply(lambda x: make_3_class(x))
df = df[:3148] # ilość reviews w zbiorze danych
print(df)

print(df['verified_reviews'][1])

show_plot(df)

print(df["rating"].value_counts())

string = ""
for i in tqdm(range(len(df['verified_reviews']))):
    string += df['verified_reviews'].iloc[i] + " "
print(len(string))

tekst = text_tokenizer(string)
bow = bag_of_words(tekst)
wordcloud(bow)


vectorizer = CountVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(df['verified_reviews'])
print(vectorizer.get_feature_names_out())
print(X_transform.toarray())
print(X_transform)
print(X_transform.shape)

show_plot_most_important(get_top_tokens(X_transform.toarray().sum(axis=0), vectorizer.get_feature_names_out(), 10),
                    bow, "Tokeny występujące najczęściej wg ilości")

print(prettytable_most_important(get_top_tokens(X_transform.toarray().sum(axis=0), vectorizer.get_feature_names_out(), 10),
                                 bow, "Tokeny występujące najczęściej wg ilości"))

vectorizer_tfidf = TfidfVectorizer(tokenizer=text_tokenizer)
transform_tfidf = vectorizer_tfidf.fit_transform(df['verified_reviews'])
columns = vectorizer_tfidf.get_feature_names_out()
weights = transform_tfidf.toarray().mean(axis=0)

show_key_plot(columns, weights)

print('Ładne tabelki\n')
print(prettytable_key(columns, weights))

x_train, x_test, y_train, y_test = train_test_split(X_transform, df['rating'], test_size=0.3, random_state=42)

classifiers = [LinearSVC(), AdaBoostClassifier(), BaggingClassifier(), DecisionTreeClassifier(), RandomForestClassifier()]
for classif in classifiers:
    fig, ax = plt.subplots(1, 1)
    classif.fit(x_train, y_train)
    y_pred = classif.predict(x_test)

    confmtx = confusion_matrix(y_test, y_pred)
    confmtx = normalize(confmtx, axis=0, norm='l1')
    display = ConfusionMatrixDisplay(confusion_matrix=confmtx, display_labels=classif.classes_)
    ax.title.set_text(f"{classif}")
    display.plot(ax=ax)
    plt.show()
    cr = classification_report(y_test, y_pred, target_names=classif.classes_)
    print(cr)

