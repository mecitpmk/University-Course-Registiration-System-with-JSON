

class User:
    USER_ID = 1
    def __init__(self,
                    name,
                    department,
                    juniorSenior,
                    id = None):
        self.name = name
        self.department = department
        self.user_id = id
        self.taking_lessons = []
        self.maxLimit = 0
        self.juniorSenior = juniorSenior
        
    def setJsonDict(self):
        return {
            'username':self.name,
            'maxLimit':self.maxLimit,
            'taking_lessons':self.taking_lessons,
            'junSen':self.juniorSenior
                }


class Course:
    COURSE_ID = 1
    def __init__(self,
                    name,
                    total_limit,
                    id=None):
        self.name = name
        self.total_limit = total_limit
        self.id = id
        self.taking_user = [] # ID TUTACAK
        self.instructor = [] # ID OLACAK
        Course.COURSE_ID += 1
    def setJsonDict(self):
        return {
                'name':self.name,
                'limit':self.total_limit,
                'taking_user':self.taking_user,
                'instructor':self.instructor}

class Instructor:
    INS_ID = 1
    def __init__(self,
                    name,
                    id=None):
        self.name = name
        self.id = id
        Instructor.INS_ID += 1
        self.giving_courses = [] # ID TUTACAK
    def setJsonDict(self):
        return {
            'name':self.name,
            'giving_courses':self.giving_courses}


class DepartmentInformations:
    def __init__(self,name,department,maxLimit):
        self.name = name
        self.department = department
        self.maxLimit = maxLimit
    def setJsonDict(self):
        return {
            self.name:{
            'id':1,
            'maxLimit':self.maxLimit
            }}
class Engineering(DepartmentInformations):
    ENG_ID = 1
    def __init__(self,name,department,maxLimit):
        DepartmentInformations.__init__(self,name,department,maxLimit)
        self.id = Engineering.ENG_ID
        Engineering.ENG_ID += 1

class Psychology(DepartmentInformations):
    PSY_ID = 1
    def __init__(self,name,department,maxLimit):
        DepartmentInformations.__init__(self,name,department,maxLimit)
        self.id = Psychology.PSY_ID
        Psychology.PSY_ID += 1
    

