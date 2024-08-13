user = input("Enter : ")  
values = list(map(int, user.split()))  

sort = True

if len(values) <=1 :
    sort = True

else :
    for i in range (1,len(values)):
        if values[i] < values[i - 1]:
            sort = False
            break

print (sort) 
