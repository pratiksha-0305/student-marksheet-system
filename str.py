class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def __str__(self):
        return f"{self.title} by {self.author} in {self.year}"
Book=Book("1984","george orwell","1950")
print(Book)
print(str(Book))        
            