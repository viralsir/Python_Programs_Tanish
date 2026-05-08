'''
dictionary : json
[] -- values -> index -> auto -> 0 -> numeric
{} -- values -> key -> manual -> user -> int,char,float,tuple -> unique -> in same dictionary
{key:value,key:value,----,key:value} -> key:value -> item
{} --> value -> manual -> int ,char,float ,tuple ,list ,dict

'''
dict={1:"one","two":2,3.0:4545.454}

print(dict)
print(dict[1])
print(dict["two"])

#insert new value
dict[4]="four"
print(dict)
dict.__setitem__("five",5)
print(dict)


#update item
dict[3.0]="three"
print(dict)

#delete item
dict.pop(4)
print(dict)
dict.__delitem__("five")
print(dict)

#view
# dict.keys()  -> []
# dict.values() -> []
# dict.item() -> [(key,value),(key,value)]
#for each

print("all keys")
for key in dict.keys():
    print(key)
print("all values")
for value in dict.values():
    print(value)
print("all keys and values")
for key,value in dict.items():
    print(key,":",value)


