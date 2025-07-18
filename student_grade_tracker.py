class Student:
    def __init__(self, name ,student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}, Avergae Grade: {self.grades}"
    
    def add_grade(self, grade):
        finally
    
    def get_average(self):
        if self.grades == 
    
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
    
    def reset_grades():

