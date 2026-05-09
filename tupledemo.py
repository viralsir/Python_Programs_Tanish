#immutable
tuple=(23,34,454,55,66)

print(tuple)
print(tuple[0])
print(tuple[-1])

print(tuple[1:3])

# tuple[0]=234
# print(tuple)

#aggretion function
print("no of element :", len(tuple))
print("max element :", max(tuple))
print("min element :", min(tuple))
print("Sum of elements :",sum(tuple))

for i in range(0,len(tuple)):
    print(tuple[i])
print("===================")
for value in tuple:
    print(value)

no=int(input("Enter the no of elements: "))
if no in tuple:
    print(no," is in tuple")
else :
    print(no," is not in tuple")
    