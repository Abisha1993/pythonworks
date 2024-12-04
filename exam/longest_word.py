def longest_word(text):
    
    words=text.split()

    longest=max(words,key=len)

    return longest
text="Hello world! This is a test for finding the longest word."

print(longest_word(text))
 