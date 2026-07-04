#   Membership operator -- test wether the value is found in a sequence
#   (Stiring, list, tuple, set or dictionary)
#   in || not in

grades = { "Spongebob": "A", 
            "Patrick": "B", 
            "Sandy": "C", 
            "Squidward": "D"}

notFound = True

while notFound:
    search = input("Search student: ").lower()

    for student in grades.keys():
        if grades.get(search.capitalize()) is None:
            print(f"Student {search} does not exist.")
            break
        else:
            if search in student.lower():
                print(f"{student} grade is {grades.get(student)}")
                notFound = False
            else:
                continue
#students = {"Nova Cryto", "Galax Galaxy", "Astra Ly"}
#
#student = input("Enter student name: ").lower
#
#if student in students:
#    print(f"{student} found!")
#else:
#    print(f"{student} is not found")

#students = {"Nova Cryto", "Galax Galaxy", "Astra Ly"}
#search = input("Enter student name: ").lower()
#
#for student in students:
#    if search in student.lower():
#        print(f"{student} found!")
#        break
#    else:
#        continue