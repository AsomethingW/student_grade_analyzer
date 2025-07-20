class Student:
    def __init__(self, name ,student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = 0
    def __str__(self):
        if self.grades == None:
            print("No grades yet")
        else:
            return f"Student: {self.name}, ID: {self.student_id}, Avergae Grade: {self.grades}"
    
    def add_grade(self, grade):
        add_number = int(input("Enter a number 1-100. "))
        if add_number >= 1 and add_number <= 100:
            for x in range(0):
                self.grades.append(f"{add_number}")
        else:
            print("N/A")        

    def has_passed(self):
        if self.grades >= 60:
            return True
        else:
            return False
    
    def get_letter_grade(self):
        if self.grades >= 90:
            return "A"
        elif self.grades >= 80 and self.grades <= 89:
            return "B"
        elif self.grades >= 70 and self.grades <= 79:
            return "C"
        elif self.grades >= 60 and self.grades <= 69:
            return "D"
        else:
            return "F"

student1 = Student(f"Kyle", "4851", list)
print(student1)

student1.add_grade(10)

student1.has_passed()

student1.get_letter_grade()

    
    def reset_grades():

