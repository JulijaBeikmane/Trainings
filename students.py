class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade:int):
        self.grades.append(grade)
    def average_grade(self):
        return sum(self.grades)/len(self.grades)


class Group(Student): 
    def __init__(self, students):
        self.students = students
    def add_student(self, student):
        self.students.append(student)
    def average_group_grade(self):
        summa = 0
        for i in range(len(self.students)):
            avg = self.students[i].average_grade()
            summa += avg
        return summa/len(self.students)
    
Human = Student("Chris", 14, [2, 7, 10] )
Human_2 = Student("Allen", 17, [8, 6, 9] )
group  = Group([Human, Human_2])
# Human.add_grade("lol")
# print(Human.average_grade())

print(group.average_group_grade())
