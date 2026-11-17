import json
new_user=[]
active_user=[]
f= open("data.json")
data=json.loads(f.read())

# for i in data:
#     print(i,data[i])
# for user in data["users"]:
#     # print(user)
#     print(f"id is {user["id"]} and name is {user["name"]} and friend is {user["friend"]} and liked_page {user["liked_page"]}")
#for user in data ["users"]:
    if user not in new_user:
        new_user.append(user)
#data["users"]=new_user
#print(new_user)
#f=open("newdata.json","w")
#f.write(json.dumps(data))
for user in data["users"]:
    if user["friend"] or user["liked_page"]:
        active_users.append(user)
        print(active_user)