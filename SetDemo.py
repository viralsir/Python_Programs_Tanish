# set1={23,23,44,55,66,77,66}
# print(set1)
#
# #insert new value
# set1.add(345)
# print(set1)
#
# #remove value
# set1.remove(345)
# print(set1)
# set1.discard(44)
# print(set1)
#
# #view data
# for value in set1:
#     print(value)
#
# #aggregration function
#
# print("no of elements :",len(set1))
# print("Maximum element :",max(set1))
# print("Minimum element :",min(set1))
# print("Sum of Element :",sum(set1))
#
# # set1.pop()
# # print(set1)
# no=int(input("Enter the no of elements: "))
# if no in set1:
#     print("Element is present on set1")
# else :
#     print("Element is not present in set1")


set1={1,2,3,4,5}
set2={3,4,5,6,7,8}

# #intersection
# set3=set1 & set2
# set4=set1.intersection(set2)
#
# print("Set3 :",set3)
# print("Set4 :",set4)


# #difference
# set3=set1 - set2
# set4=set2.difference(set1)
#
# print("Set3 :",set3)
# print("Set4 :",set4)


# #union
# set3=set1 | set2
# set4=set1.union(set2)
#
# print("Set3 :",set3)
# print("Set4 :",set4)

#Symentric diff
set3=set1 ^ set2
set4=set1.symmetric_difference(set2)

print("Set3 :",set3)
print("Set4 :",set4)




















