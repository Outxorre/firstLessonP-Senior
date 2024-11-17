#Это как у учителя
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        average = 0
        for i in self.grades:
            average += i
        
        return average / len(self.grades)

student = Student("Arlan", 14 , [5,3,3,4,5])

print(student.average_grade)