# class className:
#     # code

class vehical:
    def __init__(self,name,engine,modal):
        self.name=name
        self.engine=engine
        self.modal=modal        
        print("constructor")
    def __str__(self):
        return f"name:{self.name},\n engine:{self.engine},\n modal:{self.modal}"

class car(vehical):
    pass

v1=car("tata","v8","nexon")
v2=car("tarzan","z9","homemade")
# # v1.name="tata"
print("v1: ")
print(v1)
print("v2: \n",v2)
# print(v1.name)
# print(v1.engine)
# print(v1.modal)

# print(v2.name)
# print(v2.engine)
# print(v2.modal)
