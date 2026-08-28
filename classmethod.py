#Class methods - allow operation related to the class itself
    # Take (cls) as the first parameter, which represent the class itself
    
class Student:
    count = 0
    totalGwa = 0
    
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = gwa
        Student.count += 1
        Student.totalGwa += gwa
        
    #INSTANCE METHOD
    def getInfo(self):
        return f"Name: {self.name} | GWA: {self.gwa}"

    @classmethod
    def getStudentNum(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def getTotalGwa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Total GWA: {cls.totalGwa / cls.count:.2f}"
    
student1 = Student("Student1", 95.2)
student2 = Student("Student2", 92.7)
student3 = Student("Student3", 97.8)

print(student1.getInfo())
print(student2.getInfo())
print(student3.getInfo())
print(Student.getStudentNum())
print(Student.getTotalGwa())