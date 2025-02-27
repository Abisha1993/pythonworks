from json import load
f=open("C:\\Users\\jebin\\OneDrive\\Desktop\\pythonworks\\datasets\\booksjson.txt")
data=load(f)
for book in data:
    print(book)


# print(book)
all_titles=[book.get("title")for book in data]
print(all_titles)

#books with pages < 250

page_filter=[book.get("title")for book in data if book.get("pages")<250]
print(page_filter)

# print all_genres

all_genres=[book.get("genre") for book in data]
#print(set(all_genres))

genre_count={genre:all_genres.count(genre) for genre in all_genres}

print(genre_count)

#costly book

costly_book=max(data,key=lambda d:d.get("price"))
print(costly_book)


#author with more than one book

all_authors=[book.get("authors")for book in data]
print(all_authors)


             

