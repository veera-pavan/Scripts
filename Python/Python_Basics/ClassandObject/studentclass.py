#here were defining class(student datatype):
class student:
    def __init__ (self, name, major, is_on_probation, college, gpa):
        self.name = name,
        self.major = major,
        self.is_on_probation = is_on_probation,
        self.college = college,
        self.gpa = gpa
    
    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        

