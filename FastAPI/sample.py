class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title, author, description, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        if rating < 0:
            raise ValueError()
        else:
            self.rating = rating


book1 = Book(1, "t", 'a', 'd', 0)
print(book1.id)