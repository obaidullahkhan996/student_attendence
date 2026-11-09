students = [
    {"name": "ali", "status": "present"},
    {"name": "ahmad", "status": "absent"}
]
while True:
       print("====STUDENT ATTENDENCE TRACKER====")
       print("1. add  student")
       print("2. view students")
       print("3. mark attendence")
       print("4. attendence summary")
       print("5. exit")
                                                                                                                

       choice = input("enter your choice: ")

       if choice == "1":
              name = input("enter student name: ")
              new_student = {"name": name,"status": "absent" }
              students.append(new_student)
              print("add  a student:")

       elif choice == "2": 
              
              for student in students:
                     print(student["name"], "-", student["status"])
                    #  print(student["name"]) 
                    #  print(student["status"]) 
       elif choice == "3":
              name = input("enter mark attendence!").strip().lower()
              found = False
              for student in students:
                     
                    if student["name"].lower() == name:
                       student["status"] = "present"
                       print("mark attendence")
                       found = True

              if not found:
                          print("student not found") 

       elif choice == "4":
              total = 0
              present = 0
              absent = 0
              for student in students:
                     total += 1

                     if student["status"] == "present":
                            present += 1

                     elif student["status"] == "absent":
                            absent += 1

              print("total students: ", total)
              print("present students:", present)
              print("absent students:", absent)
                     

                     
                          

       elif choice == "5":
              print("thank you!")
              break   