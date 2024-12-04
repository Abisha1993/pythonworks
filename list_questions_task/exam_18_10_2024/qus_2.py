def max_word(text):
    words=text.split()
    max_len_word=max(words,key=len)
    return max_len_word,len(max_len_word)
text="this is a simple question return word with maximum number of chaeacters"
word,length=max_word(text)
print(max_word)