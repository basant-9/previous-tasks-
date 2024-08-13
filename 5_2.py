values = input ("Enter : ")
lst = list(map(int, values.split()))  
n = int(input("enter :"))

if len(values) < 4:
    print("Error") 
else:
    removed  = [] 
    for i in range(n,len(values)):
        removed.append(values[i])

    print(removed)  