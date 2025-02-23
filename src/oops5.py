class Book:
    def __init__(self, title, author, pages):
        print('Book created')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return ('Title: %s, Author:%s and pages:%s' % (self.title, self.author, self.pages))

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Book is deleted')


if __name__ == "__main__":
    book = Book('Python', "Jose_", 100)
    print(book)
    print(len(book))
    book.__del__()
    print(book)
