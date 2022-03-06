import re

# ZADANIE 1.
# a.
text1 = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"  # string

cousunac1 = '[0-9]'  # pattern  lub r'\d' ale może też być bez trgo r przy r'[0-9]' -> raw string

# result = re.sub(pattern, repl, string, count=0, flags=0);

# repl -> czym zastępujemy

wynik1 = re.sub(cousunac1, '', text1, count=0, flags=0)

print(text1)
print(wynik1)

# b.
text2 = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"

cousunac2 = '(<([^>]+)>.*?)'

wynik2 = re.sub(cousunac2, '', text2, count=0, flags=0)

print(text2)
print(wynik2)

# c.
text3 = "Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus eu risus."  # string

cousunac3 = '[,;\.]'  # pattern

# result = re.sub(pattern, repl, string, count=0, flags=0);

# repl -> czym zastępujemy

wynik3 = re.sub(cousunac3, '', text3, count=0, flags=0)

print(text3)
print(wynik3)

# ZADANIE 2.
text4 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus."

wynik4 = re.findall('#[a-z]+', text4)

print(wynik4)

# ZADANIE 3.
text5 = "Lorem ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta; lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-)."

wynik5 = re.findall('[:;]-?[)(><]', text5)  # '\W{2,3}[^\s]' lub [:;][)(<>]|[:;][-][)(<>] lub [:;]-{0,1}[)(><]

print(wynik5)
