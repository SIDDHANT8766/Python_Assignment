# Imp :-  Increase class variable by 1 when next object is created


class BookStore:
    NoOfBooks = 0

    def __init__(self,A,B):
        self.Name = A
        self.Author = B
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}")
        print("Number of Books : ",BookStore.NoOfBooks)

    
obj1 = BookStore("Linux System Programming","Robert Love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Ritchie")
obj2.Display()

