#
class person:
    def __init__(self,name):
        self.name=name
        # print("constructor")

    def __str__(self):
        return f"name :{self.name}"

class student(person):
    def  __init__(self,name,cls, schoolname, section):
        super().__init__(name)
        # person.__init__(self,name)
        self.cls=cls
        self.schoolname=schoolname
        self.section=section

    def __str__(self):
        return f"{super().__str__()}\n cls:{self.cls} \n schoolname:{self.schoolname} \n sectioin:{self.section}"
        # return f"{person.__str__(self)}\n cls:{self.cls} \n schoolname:{self.schoolname} \n sectioin:{self.section}"

class empolyee(person):
    def __init__(self,name,company,designation):
        super().__init__(name)
        self.company=company
        self.designation=designation
    def __str__(self):
        return f"{super().__str__()}\n company:{self.company}\n designation:{self.designation}"


p1=person("rakesh")
print("p1:\n", p1)

s1=student("ravi","9","h d public school","a")
print("s1:\n", s1)

e1=empolyee("ravi","tcs","manger")
print("e1:\n",e1)