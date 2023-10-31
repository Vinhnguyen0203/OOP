class Person:
    def __init__(self,fName,lName,occupation,dob):
        self.fName=fName
        self.lName=lName
        self.occupation=occupation
        self.dob=dob
    def getname(self):
        pass
    def setname(self):
        pass
    def details(self):
        pass
class Student(Person):
    # def __init__(self,name,Class,major):
        # super().__init__(fName,lName,
        # self.Class=Class
        # self.major=major
    def __init__(self,fName,lName,occupation,dob,major):
        super().__init__(fName,lName,occupation,dob)
        self.major=major
        self.courseList=[]
    def getname(self):
        print(f"the name of student is {self.name}")
    def setname(self,newname):
        self.name=newname
        print(f"the new name is {self.name}")
    def details(self):
        print(f"the details is {self.name} class: {self.Class} major :{self.major}")
    def adding(self,course):
        self.courseList.append(course)
    def print_courselist(self):
        for course in self.courseList:
            print(course)
class Teacher(Person):
    def __init__(self,fName,lName, major):
        super().__init__(fName,lName,"",major)
        self.courses=[]
        self.students=[]
    def addCourse(self,course):
        self.courses.append(course)
    def addStudent(self,student):
        self.students.append(student)
    def print_details(self):
        print(f"Teacher:{self.fName}")
        print("Courses")
        for course in self.courses:
            print(course)
        for student in self.students:
            print(student.fName)
# vinh=Student("vinh","A","IT")
# vinh.setname("huy")
# vinh.details()
vinh=Student("The vinh","Nguyen","Student",2,"IT")
vinh.adding("math")
vinh.adding("physics")
vinh.adding("history")
Timo=Teacher("abc","bcd",'IT')
vinh.adding("IT")
Timo.addCourse("IT")
Timo.addStudent(vinh)
# Timo.print_details()
huy=Student('khai huy','truong',"student","2","IB")
huy.adding("IT")
Timo.addStudent(huy)
Timo.print_details()


