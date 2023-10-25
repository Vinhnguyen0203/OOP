class Author:
    def __init__(self,name:str):
        self.name=name
        print(f"Author: {self.name}")
    def __str__(self):
        return self.name
class Book:
    def __init__(self):
        self.list=[]

    def  adding(self,nameofbook:str):
        return self.list.append(nameofbook)


first_author=Author("J.K.Rowling")
book1=Book()
print(book1.adding("Harry Potter"))
book1.adding("I donot know")
