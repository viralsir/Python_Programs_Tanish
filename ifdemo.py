'''
   if syntax
       if (condition) :
            true part
            statement
        else :
            statement;
            false part
  i)if else
  ii)elif
  iii)nested if

   logical operator
   operator             symbol
   and                  and
   or                   or
   not                   not

'''
no1=int(input("enter no1"))
no2=int(input("enter no2"))
no3=int(input("enter no3"))

if no1>0 and no2>0 and no3>0:

    if no1>no2 and no1>no3:
        print(no1," is a maximum number")

    elif no2>no1 and no2>no3 :
        print(no2," is a maximum number")
    else :
        print(no3," is a maximum number")
else :
    print("invalid input")







