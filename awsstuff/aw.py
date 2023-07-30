
#how to build a class and add standard methods to it

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def  average(self):
        return self.grade
    def  is_pass(self):
        if self.grade>40:
            return True
        else:
            return False
#how to create an object of the class

student1=Student("Rohan",212,10)

print(student1.name)

print(student1.age)

print(student1.average())

print(student1.is_pass())

#real life application of the code above


class Car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def  is_old(self):
        if self.year>2000:
            return True
        else:
            return False
        




        
        


