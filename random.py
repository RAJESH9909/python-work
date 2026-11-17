l=[1,1,1,2,2,3,3,3,4,4,4,5]
count=0
for i in range(1,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            count=count+1
            if count==1:
                
                print(l[i]," ",count)
