class Members:#Student - Name ID, elective subject(0 or more but not more than 5)
    def __init__(self,id,name):
        self.ID = id
        self.Name = name
        
class Student(Members):
    def __init__(self,id,name,elective_Subject):
        Members.__init__(self,id,name)
        self.sub = elective_Subject
    def display(self):
        print(self.Name)
        print(self.ID)
        print(self.sub)        
        
class Faculty(Members):
    pass #faculty-ID Name , specialisation  one proff max 70 student 3 sub at max  Mapping schedule
        
class mapping:
    #practically make ffcs (Think of making an UML)
    pass        
        
