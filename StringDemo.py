name="hello welcome to the world of python 3.2"
print(name)
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])

print(name[0:5])

print("no of character :",len(name))
print("max character :",max(name))
print("min character :",min(name))
print(float(name[-3:]))

name1="amit"
name2="Shah"
name3=name1+name2
print(name3)
name4=name1*3
print(name4)
# char=input("enter characters:")
# if char in name:
#     print(char , " is in string")
# else:
#     print(char,"is not in string")

# name[1]='t'
# print(name)

name5=name.replace("hello","hi")
print(name5)

print(name.lower())
print(name.upper())
print(name.split('t'))
print(name.count('t'))
print(name.find('t',15))

for character in name:
    if character.isalpha():
        print(character,"-","is alphabet")
    elif character.isdigit():
        print(character,"-","is digit")
    elif character.isspace():
        print(character,"-","is space")
    else :
        print(character,"-","is symbol")


name1="amit"
name2="Shah"
name3=name1.join(name2)
print(name1)
print(name2)
print(name3)


