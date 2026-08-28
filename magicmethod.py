#Magic methods = allow developers to define of customize the behavior  of objects
# __init__, __str__, __eq__

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"Title: {self.title} | Author: {self.author}"
    
    def __eq__(self, otherBook):
        return "Books are the same" if self.title == otherBook.title and self.author == otherBook.author else "Books are not the same"
    
    def __lt__(self, otherBook):
        return self.pages < otherBook.pages
    
    def __gt__(self, otherBook):
        return self.pages > otherBook.pages
    
    def __add__(self, otherBook):
        return f"{self.pages + otherBook.pages} total added pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"{key} is not found"
        
book1 = Book("Game of Thrones", "Person", 1252)
book2 = Book("Game of Thrones", "Person", 2451)
book3 = Book("A Knight of the Seven Kingdoms", "Person", 727)

print(book1)
print(book2)
print(book3)
print(book1 == book2)
print(book2 < book3)
print(book2 > book3)
print("Knight" in book3)
print(book2["nega"])