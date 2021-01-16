import json
import jsonCreator
import os

class System:
    def foundLimits(self,department,juniorSenior):
        try:
            with open("departmentJson.json") as js:
                data = json.load(js)
                max_limit = data.get(department).get(juniorSenior).get("maxLimit")
                return max_limit
        except:
            return 0
    
    def addDepartment(self,departmentObject):
        if "departmentJson.json" not in os.listdir():
            with open("departmentJson.json","w+") as f:
                js = {departmentObject.department:departmentObject.setJsonDict()}
                json.dump(js,f,indent=4)
        else:
            with open("departmentJson.json","r+") as f:
                current_json = json.load(f)
                if current_json.get(departmentObject.department) is None:
                    d = {departmentObject.department:departmentObject.setJsonDict()}
                    current_json.update(d)
                else:
                    will_up = current_json.get(departmentObject.department)
                    will_up.update(departmentObject.setJsonDict())
                f.seek(0)
                json.dump(current_json,f,indent=4)
    def addNewUser(self,user_object,update=False):

        if "departmentJson.json" in os.listdir():
            print("")
            user_object.maxLimit = self.foundLimits(user_object.department,user_object.juniorSenior)
        if "userJsons.json" not in os.listdir():
            with open("userJsons.json","w+") as f:
                if user_object.user_id == None:
                    rand = 1
                else:
                    rand = user_object.user_id
                new_dict = {user_object.department:{rand:user_object.setJsonDict()}}
                json.dump(new_dict,f,indent=4)
        else:
            with open("userJsons.json","r+") as f:
                current_json = json.load(f)
                if current_json.get(user_object.department) is not None:
                    will_update = current_json.get(user_object.department)
                    if not update:
                        if user_object.user_id == None:
                            rand_id = str(int(max(will_update))+1)
                        else:
                            rand_id = user_object.user_id
                        will_update.update({rand_id:user_object.setJsonDict()})
                    else:
                        will_update.update({update:user_object.setJsonDict()})
                else:
                    if user_object.user_id is None:
                        rand = 1
                    else:
                        rand = user_object.user_id
                    current_json.update({user_object.department:{rand:user_object.setJsonDict()}})
                f.seek(0)
                json.dump(current_json,f,indent=4)
    
    
    def addInsorCourse(self,course=False,instructor=False,update=False):
        
        if course:
            current_object = course
            js_name = "courseJson.json"
        else:
            current_object = instructor
            js_name = "instJson.json"
        
        
        if js_name not in os.listdir():
            with open(js_name,"w+") as f:
                if current_object.id == None:
                    rand = 1
                else:
                    rand = current_object.id
                js = {rand:current_object.setJsonDict()}
                json.dump(js,f,indent=4)
        else:
            with open(js_name,"r+") as f:
                current_json = json.load(f)
                if not update:
                    if current_object.id == None:
                        rand = str(int(max(current_json))+1)
                    else:
                        rand = current_object.id
                    current_json.update({rand:current_object.setJsonDict()})
                else:
                    current_json.update({update:current_object.setJsonDict()})
                f.seek(0)
                json.dump(current_json,f,indent=4)
    def addCourseToUser(self,courseOb,studentOb):
        studentOb.taking_lessons.append(courseOb.id)
        courseOb.taking_user.append(studentOb.user_id)
        self.addInsorCourse(course=courseOb,update=courseOb.id)
        self.addNewUser(studentOb,update=studentOb.user_id)
    def giveCoursetoInst(self,instObject,courseObj):
        instObject.giving_courses.append(courseObj.id)
        courseObj.instructor.append(instObject.id)
        self.addInsorCourse(instructor=instObject,update=instObject.id)
        self.addInsorCourse(course=courseObj,update=courseObj.id)
    

if __name__ == "__main__":
        
    syst = System()
    """
        Important notes : when lesson, or user , or instructor created, id is not compulsory to given
        HOWEVER!
            When try to add user to course, id is very important. Because json object stores id of lesson.
            EX->
                    "1499": {
                                "name": "System Communucation",
                                "limit": 150,
                                "taking_user": [
                                    "44"
                                ],
                                "instructor": [
                                    "221"
                                ]
                            }
            It means that when you try to implement this code in GUI or real life,
            You have to match your course object corresponding to json obect.
    """
    engineering_dep = jsonCreator.Engineering("Freshman","Engineering",10) # 10 course maximum limit for Engineering,Freshman Student
    mecit = jsonCreator.User("Musti","Engineering","Freshman","44")
    lesson = jsonCreator.Course("System Communucation",150,"1499") 
    teacher  = jsonCreator.Instructor("Cem Unsalan","221")

    ## TO SEE SYSTEM , COMMENT OUT THOSE..##

    # syst.addDepartment(engineering_dep)
    # syst.addNewUser(mecit)
    # syst.addInsorCourse(course=lesson)
    # syst.addInsorCourse(instructor=teacher)


    # syst.addCourseToUser(lesson,mecit)
    # syst.giveCoursetoInst(teacher,lesson)

