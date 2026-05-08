# person={"name":"vimal","age":22,"city":"Mumbai","phone number":{"home":9812312345,"office":97123453}}
# print(person)
# print(person["name"])
# print(person["age"])
# print(person["city"])
# print(person["phone number"]["home"])
# print(person["phone number"]["office"])



# xml ->   <name>vimal</name> <age>23</age>   (webservice)
# json -> {"name":"vimal"}
# stand=[{}, {"A":[],"B":[]}]

stand={ "0":{"A":[], "B":[]},
        "2":{"A":[], "B":[]},
       }
option2=0
while option2!=3:

students={"A":[
          {"rollno":1,"name":"vimal","maths":34,"science":45},
          {"rollno":2,"name":"vijay","maths":44,"science":45}
         ],"B":[
            {"rollno":1,"name":"vimal","maths":34,"science":45},
          {"rollno":2,"name":"vijay","maths":44,"science":45}
            ]
        }
print(students["A"][0]["name"])
# print(students[0]["name"])
# print(students[0]["maths"])
# print(students[0]["science"])
# print(students[1]["name"])
# print(students[1]["maths"])
# print(students[1]["science"])
