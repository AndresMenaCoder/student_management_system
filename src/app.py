
from services import register_student , consult_students , search_student , actualize_Student , delete_student

students = []


while True:
    try:
        print("------Menu------")
        print("1. Register students")
        print("2. Consulter list of students")
        print("3. Search students")
        print("4. Actualize students")
        print("5. Delete students")
        print("6. exit")
    
        option = int(input("please select a option: "))
        
        if option == 1:
            Name = input("Please enter your name: ")
            Age = int((input("Please enter your age: ")))
            Course = input("Please enter your course: ")
            Status = input("Please enter your status(Active/Inactive): ")
            print("The student has registered")
            
            register_student(students,Name,Age,Course,Status)
                    
        
        elif option == 2:
            consult_students (students)
        
        
        elif option == 3:
            id_search = int(input("Please enter your studen ID: "))
            result = search_student(students,id_search)
            
            if result:
                print("The student's ID has been found")
                print(result)
            else:
                print("The student ID could not be found")

        
        elif option == 4:
            id_search = int(input("Please enter your ID: ")) -1
            New_name = input("please enter your name: ")
            New_age = int(input("Please enter your New age: "))
            New_course = input("Please enter your New course: ")
            New_status = input("Please enter your New Status: ")
            result = actualize_Student(students,id_search,New_name,New_age,New_course,New_status)
            
            if result:
                print("The data has been updated")
            else:
                print("The have't updated the data")
        
        
        elif option == 5:
            id_search = int(input("Please enter your ID: ")) -1
            result = delete_student(students,id_search)
            
            if result:
                print("The students has been removed")
            else:
                print("The student could not be found")
        
        elif option == 6:
            break
        
        else:
            print("option invalid, please select a of the option avaible")
    except ValueError:
        print("Value invalid, please select a of the option avaible")