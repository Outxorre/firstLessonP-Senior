class Calculator:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return x + y

    def substract(self, x, y):
        return abs(self.x - self.y) #abs - отнятие меньшего от большего

    def divide(self, x, y):
        return self.x / self.y

    def multiply(self, x, y):
        return self.x * self.y

calculator = Calculator(4,5)
print(calculator.add(2,1))
print(calculator.divide(6,2))

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print("Название-", self.title , "  Автор-",self.author,"  Год издания-",self.year) #ну или же print(f"Название: {self.title} \n Автор: {self.author} \n Год Выпуска: {self.year}")

book1 = Book("Book1", "My Grandfather", "1987")
book1.display_info()