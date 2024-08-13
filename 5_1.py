user = input("Enter items :")
items = user.split ()
output = ''
if not items:
    output = ''
elif len(items) == 1:
    output = items[0]
elif len(items) == 2 :
    output = items[0] + ' and ' + items[1]
else :
    for i in range (len(items)):
        if i == len(items) - 1:
            output += 'and' + items[i]
        else :
          output += items[i] +  ","
print(output) 