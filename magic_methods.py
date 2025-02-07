class Author:
    def __init__(self, name, book_name, pages):
        self.name = name
        self.book_name = book_name
        self.pages = pages

    def __len__(self):
        return self.pages
    def __call__(self, *args, **kwargs):
        print("Hi")
    def __del__(self):
        print("Author object has been deleted")
    def __str__(self):
        return f"{self.book_name} by {self.name}"

d = Author("Joshua", "Python Basic to Advance", 43)
print(d)
print(len(d))
d()
del d
