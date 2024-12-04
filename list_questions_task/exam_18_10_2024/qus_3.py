from collections import Counter
def most_frequent_word(text):
    words=text.lower().split()
    word_counts=count(words)
    most_common_word,frequency=word_counts.most_common(1)[0]
    return most_common_word,frequency
text="this is a simple python program that print most recursive word. This is simple"
word,count=most_frequent_word(text)
print(most_frequent_word)

