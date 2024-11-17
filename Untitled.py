from operator import mod


class Car:
    def __init__(self, brand, model, year, HP):
        self.brand = brand         #Точка селф - сыллка. Она может быть любой, это обращение. Тут - файл обращается к себе и создает переменную у себя
        self.model = model
        self.year = year
        self.HP = HP
    
    def maxSpeed(self):
        print(self.brand, "Максимальая скорость бренда - 230 км/час")


car1 = Car("Toyoto", "Carmy", 2012, 10)
print(car1.brand)
print(car1.model)
print(car1.year)
print(car1.HP)