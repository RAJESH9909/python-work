users=[
    {
        "name":"raja",
        "email":"raja123@gmail.com",
        "password":"raka@1123"
    },
    {
        "name":"ravi",
        "email":"ravi123@gmail.com",
        "password":"ravi_321",

    },
    {
        "name":"raka",
        "email":"rakaraka@gmail.com",
        "password":"432rakaraka"

    },
    
]
def login():
    email=""
    password=""
    for user in users:
        if(email==user["email"] password==user["password"]):
            login sussessfull

def register():
    email=""
    name=""
    password=""
    
q=""
while q!="0":
    print("press 1 for login")
    print("press 2 for register")
    print("press  for register")
    q=input("enter mode")
    if(q==0):
        print("exiting...")
        break
    elif(q=="1"):
        login()