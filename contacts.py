contacts = {
    "number" : 4,
    "students" : [
        {"name" : "Janardhan", "email" : "janardhan@gmail.com"} ,
        {"name" : "Jenny", "email" : "jenny@gmail.com"} ,
        {"name" : "tillu", "email" : "tillu@gmail.com"} ,
        {"name" : "mango", "email" : "mango@gmail.com"} 
    ]
}

for student in contacts["students"]:
    print(student["email"])

