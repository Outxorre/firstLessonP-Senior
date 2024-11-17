class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        print(int(sum(self.grades)/len(self.grades)))
        


list1 = [5,3,3,4,5]
student1 = Student("Arlan",12,list1)
student1.average_grade()


