class student:

    def __init__(self,schoolname,schooladdress,department,leadername,studentname,id,address,credit,gpa):
        self.schoolname = schoolname
        self.schooladdress = schooladdress
        self.department = department
        self.leadername = leadername
        self.studentname = studentname
        self.id = id
        self.address = address
        self.credit = credit
        self.gpa = gpa

  
    def getSchoolName(self):
        return self.schoolname
    def setSchoolName(self, new_schoolname):
        self.schoolname = new_schoolname

    def getschooladdress(self):
        return self.schooladdress
    def setschooladdress(self,new_schooladdress):
        self.schooladdress = new_schooladdress

    def getDepartment(self):
        return self.department
    def setDepartment(self, new_department):
        self.department = new_department
    
    def getDirectorName(self):
        return self.leadername
    def setDirectorName(self, new_leadername):
        self.leadername = new_leadername
    
    def getStudentName(self):
        return self.studentname
    def setStudentName(self, new_studentname):
        self.studentname = new_studentname
    
    def getStudentID(self):
        return self.id
    def setStudentID(self, new_id):
        self.id = new_id
    
    def getAddress(self):
        return self.address
    def setAddress(self, new_address):
        self.address = new_address

    def getCredits(self):
        return self.credits
    def setCredits(self, new_credits):
        self.credits = new_credits

    def getGPA(self):
        return self.gpa
    def setGPA(self, new_gpa):
        self.gpa = new_gpa
        
#建立物件
student1 = student("stust","NT St","Computer Science and Information Engineering","Gwo-Jiun Horng","Yue-Ting Pan","4b0g0051","4b0g0051@stust.edu.tw",100,3.2)
#呼叫副函式
print(student1.getSchoolName())

student1.setSchoolName("南台科技大學")
#呼叫副函式
print(student1.getSchoolName())