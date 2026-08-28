#Class variables - shared among all the instances of a class
                # defined outside the constructor
                
                
                
class Student:
    numberOfStudents = 0
    schoolYear = 2026
    
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        Student.numberOfStudents += 1
        
student1 = Student("Codex", 18, 1001)
student2 = Student("Nova", 18, 1002)
student3 = Student("Thorfinn", 18, 1003)
student4 = Student("Thors", 18, 1004)

print(f"-------- School Year {Student.schoolYear} --------")
print(f"Name: {student1.name} | Age: {student1.age} | ID: {student1.id}")
print(f"Name: {student2.name} | Age: {student2.age} | ID: {student2.id}")
print(f"Name: {student3.name} | Age: {student3.age} | ID: {student3.id}")
print(f"Name: {student4.name} | Age: {student4.age} | ID: {student4.id}")
print(f"Total Students: {Student.numberOfStudents}")