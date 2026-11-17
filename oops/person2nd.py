"""
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
"""        