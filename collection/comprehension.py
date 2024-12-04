text=["apple","iphone","orange","potato"]

#words starting with wowels

wowel_words=[w for w in text if w[0] in ['a','e','i','o','u']]

print(wowel_words)

#cosonant_words

consonant_words=[w for w in text if w[0]  not in ['a','e','i','o','u']]

print(consonant_words)




#longest words

long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]

print(longest_words)