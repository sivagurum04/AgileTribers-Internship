import os
cources_available =("Python", "Data Science", "Web Development", "AI & ML")
def add_student():
    try:
        student_id=input("Enter the id of student :")
        student_name=input("Enter the name of the student :")
        age=int(input("Enter the age :"))
        print("available_cource :" ,cources_available)
        cource_enrolled=input("Enter the cource to enroll").split(",")
        cource_enrolled=set([cource.strip() for cource in cource_enrolled if cource.strip() in cources_available])
        total_fees = float(input("Enter Total Fees: "))
        fees_paid = float(input("Enter Fees Paid: "))
        balance = total_fees - fees_paid
        student = {
            "ID": student_id,
            "Name": student_name,
            "Age": age,
            "Courses": cource_enrolled,
            "Total Fees": total_fees,
            "Fees Paid": fees_paid,
            "Balance": balance
        }
        with open("students.txt","a") as f:
            f.write(str(student)+"\n")
            print(f"student {student_name} added succesfully \n")
    except ValueError:
        print("value error(Invalid data)")
def view_students():
    try:
        with open("students.txt","r") as f:
            lines = f.readlines()
        if not lines:
            print("No student record found")
            return
        else:
            print("student records ")
            for line in lines:
                student =eval(line.strip())
                print(f"ID: {student['ID']}")
                print(f"Name: {student['Name']}")
                print(f"Age: {student['Age']}")
                print(f"Courses Enrolled: {', '.join(student['Courses'])}")
                print(f"Total Fees: ₹{student['Total Fees']:,}")
                print(f"Fees Paid: ₹{student['Fees Paid']:,}")
                print(f"Balance: ₹{student['Balance']:,}")
    except FileNotFoundError:
        print("file not found")            
    except Exception as e:
        print(f"error as {e}")  
def update_student():
    student_id = input("Enter the Student ID to update: ")
    updated = False

    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()

        with open("students.txt", "w") as f:
            for line in lines:
                student = eval(line.strip())
                if student["ID"] == student_id:
                    print("Current details:", student)
                    student["Name"] = input("Enter new name: ")
                    student["Age"] = int(input("Enter new age: "))
                    new_courses = input("Enter new courses (comma-separated): ").split(",")
                    student["Courses"] = set([c.strip() for c in new_courses if c.strip() in cources_available])
                    student["Total Fees"] = float(input("Enter new total fees: "))
                    student["Fees Paid"] = float(input("Enter new fees paid: "))
                    student["Balance"] = student["Total Fees"] - student["Fees Paid"]
                    updated = True
                    print("Student updated successfully.")
                f.write(str(student) + "\n")

        if not updated:
            print("Student ID not found.")
    except Exception as e:
        print(f"Error updating student: {e}")
def remove_student():
    student_id = input("Enter the Student ID to remove: ")
    found = False

    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()

        with open("students.txt", "w") as f:
            for line in lines:
                student = eval(line.strip())
                if student["ID"] != student_id:
                    f.write(str(student) + "\n")
                else:
                    found = True

        if found:
            print(f"Student ID {student_id} removed successfully.")
        else:
            print("Student ID not found.")
    except Exception as e:
        print(f"Error removing student: {e}")
def generate_fee_report():
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
        print("Students with Pending Fee Payments:\n")
        for line in lines:
            student = eval(line.strip())
            if student["Balance"] > 0:
                print(f"{student['Name']} (ID: {student['ID']}) - Balance: ₹{student['Balance']:,}")
    except FileNotFoundError:
        print("Student data file not found.")
    except Exception as e:
        print(f"Error generating fee report: {e}")
add_student()
update_student()
view_students()
remove_student()
generate_fee_report()