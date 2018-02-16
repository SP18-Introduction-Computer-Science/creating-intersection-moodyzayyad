a = [1,4,5,7,8,12]

b = [4,5,9,12,15,2]

c = []

def intersect(list1, list2):
    for element in list1:
        if element in list2:
            c.append(element)
    return c

output = intersect(a,b)
print ("output: ")
for i in output:
    print(i)
