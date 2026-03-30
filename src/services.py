def register_student (students,Name,Age,Course,Status):
    
    if Age <= 0:
        print("You cannot add negative or zero age")
        return False
    
    if len(students) == 0:
        new_id = 1
    else:
        new_id = students[-1]["id"] + 1
    
    student = {
        
        "id" : new_id ,
        "Name" : Name ,
        "Age" : Age ,
        "Course" : Course ,
        "Status" : Status
    }
    students.append(student)
    return True


def consult_students (students):
    if len(students) == 0:
        print("The are no registered students")
    else:
        for student in students:
            print(f"ID: {student['id']} |  Name: {student['Name']} | Age: {student['Age']} | Course: {student['Course']} | Status: {student['Status']}")

def search_student(students,id_search):
    for student in students:
        if student["id"]  == id_search:
            return student
    return None

def actualize_Student(students,id_search,New_name,New_age,New_course,New_status):
        student = search_student(students,id_search)
            
        if student:
                if New_age <= 0:
                    print("Age invalide")
                    return False
                    
                student["Name"] = New_name
                student["Age"] = New_age
                student["Course"] = New_course 
                student["Status"] = New_status 
                return True
                
        else:
                return False
        
            

def delete_student(students,id_search):
    student = search_student(students,id_search)
    if student:   
        students.remove(student)
        return True
    else:
        return False