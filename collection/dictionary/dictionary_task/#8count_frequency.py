sentence="this is a test sentence this sentence is just a test"

def count_word_frequencies(sentence):
    words=sentence.split()
    word_frequencies={}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word]+=1
        else:
            word_frequencies[word]=1
            return word_frequencies
        sentence="this is a test sentence,This sentence is just a test."
        print(count_word_frequencies(sentence))
