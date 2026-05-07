'''

 array : list  (class)
         list (datastructure) -> index  0 , 1, 2, ---,N
         list -> [2,"Vimal",343.34]
 array : insert , update ,search , delete
 special feature

forward index -> 0,1,2,--,N
backward index -> -1,-2,-3-, -- -N
# '''
# nolist=[12,23,44,55]
# print(nolist)
# print(nolist[0])
# print(nolist[1])
# print(nolist[-2])
# print(nolist[-1])
#
# #insert data into list
# #nolist[4]=34;
# nolist.append(666)
# nolist.append(777)
# nolist.append(int(input("Enter No:")))
# print(nolist)
# nolist.insert(2,157)
# nolist.insert(-2,157)
# print(nolist)
#
# #update data into list
# nolist[4]=34;
# print(nolist)
#
#
# #delete data into list
#
# #remove by value
# nolist.remove(157)
#
# #remove by index
# #nolist.pop()
# nolist.pop(0)
# print(nolist)

# nolist=[34,44,543,324,223,33]
# #view element of list
# print(nolist)
#
# #view by while loop
# print("using while loop")
# index=0
# while index<len(nolist):
#     print(nolist[index])
#     index+=1
#
# print("using for iterator loop")
# #view by for loop
# for index in range(0,len(nolist)):
#     print(nolist[index])
#
# print("using for each loop")
# #view by for each loop
# for value in nolist:
#     print(value)

#special feature

# nolist=[23,"vimal",3434.34]

# print(nolist)
# print(nolist[0])
# print(nolist[1])

#nolist=[23,33,44,5,66,44]
#inbuilt function
#aggregration function
# print("no of elements :", len(nolist))
# print("max of elements :", max(nolist))
# print("min of elements :", min(nolist))
# print("sum of elements :", sum(nolist))
#
# #inbuilt function
# print("44 in nolist :", nolist.count(44))
# # nolist.reverse()
# # print(nolist)
# nolist.sort(reverse=True)
# print(nolist)
#
# list1=[1,2,3,4,5]
# list2=list1.copy()
# list1.append(6)
# print(list1)
# print(list2)

#slicing
# list1=[32434,44,53,3,23,4534,545]
# print(list1[2:5])
# print(list1[2:])
# print(list1[:2])
# print(list1[:])
# print(list1[0:5:2])
# print(list1[-3:-1])
# print(list1[-3:])

list2=[2,3,5]
# list3=list1+list2
# list1.extend(list2)
# print(list3)
# print(list1)

#nested list
# list1.append(list2)
# print(list1)
# print(list1[-1])
# print(list1[-1][0])

# list3=list1*2
# print(list3)


#list comprehension
nolist=[x for x in range(10)]
print(nolist)
nolist=[x**2 for x in range(10)]
print(nolist)
nolist=[x for x in range(10) if x%2==0]
print(nolist)
maths_marks_list=[34,34,44,5,6,77,78,74]
pass_maths_mark_list=[x for x in maths_marks_list if x>34]  # R
print(pass_maths_mark_list)






