# import mysql.connector
# import matplotlib.pyplot as plt


# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="student"
# )

# cursor = db.cursor()

# while True:
#     print("\n1. View all students")
#     print("2. Add a new student")
#     print("3. Graph")
#     print("4. pie chart")
#     print("5.percentage graph")
#     print("6. subject average graph")
#     print("7. grade distribution graph")
#     print('8.user input')
#     print("9. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         cursor.execute("SELECT * FROM students_data")
#         data = cursor.fetchall()

#         print("\nStudent Details:")
#         for row in data:
#             print("Name:", row[1])
#             print("Roll Number:", row[2])
#             print("Gender:", row[3])
#             print("Maths:", row[4])
#             print("Science:", row[5])
#             print("English:", row[6])
#             print("Social Science:", row[7])
#             print("Total:", row[8])
#             print("Percentage:", row[9])
#             print("Grade:", row[10])
#             print("Result:", row[11])

#     elif choice == '2':

#         students_name = input("Enter student name: ")

#         while True:
#             student_roll_no = input("Enter student roll number: ")

#             if not student_roll_no.isdigit():
#                 print("Invalid input. Please enter a numeric value for student roll number.")
#                 continue

#             cursor.execute("SELECT * FROM students_data WHERE roll_no=%s", (student_roll_no,))
#             result = cursor.fetchone()

#             if result:
#                 print("Roll number already exists! Please enter a different roll number.")
#             else:
#                 break

#         student_gender = input("Enter student gender: ")

#         maths_marks = input("Enter marks in maths: ")
#         while not maths_marks.isdigit() or not (0 <= int(maths_marks) <= 100):     
#             print("Invalid input.")
#             maths_marks = input("Enter marks in maths: ")

#         science_marks = input("Enter marks in science: ")
#         while not science_marks.isdigit() or not (0 <= int(science_marks) <= 100):
#             print("Invalid input.")
#             science_marks = input("Enter marks in science: ")

#         english_marks = input("Enter marks in english: ")
#         while not english_marks.isdigit() or not (0 <= int(english_marks) <= 100):
#             print("Invalid input.")
#             english_marks = input("Enter marks in english: ")

#         social_science_marks = input("Enter marks in social science: ")
#         while not social_science_marks.isdigit() or not (0 <= int(social_science_marks) <= 100):
#             print("Invalid input.")
#             social_science_marks = input("Enter marks in social science: ")

#         maths_marks = int(maths_marks)
#         science_marks = int(science_marks)
#         english_marks = int(english_marks)
#         social_science_marks = int(social_science_marks)

#         total_marks = maths_marks + science_marks + english_marks + social_science_marks
#         percentage = (total_marks / 400) * 100

#         if percentage >= 90:
#             grade = "A+"
#         elif percentage >= 80:
#             grade = "A"
#         elif percentage >= 70:
#             grade = "B"
#         elif percentage >= 60:
#             grade = "C"
#         else:
#             grade = "D"

#         if grade == "D":
#             result = "Fail"
#         else:
#             result = "Pass"

#         sql = """INSERT INTO students_data(student_name, roll_no, gender, maths, science, english, social_science, total, percentage, grade, result)
#         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

#         values = (
#             students_name, student_roll_no, student_gender,
#             maths_marks, science_marks, english_marks, social_science_marks,
#             total_marks, percentage, grade, result
#         )

        

#         cursor.execute(sql, values)
#         db.commit()

#         subjects = ["Maths", "Science", "English", "Social Science"]
#         marks = [maths_marks, science_marks, english_marks, social_science_marks]

#         plt.bar(subjects, marks, color=["blue","green","orange","red"])
#         plt.title("Student Subject-wise Marks")
#         plt.xlabel("Subjects")
#         plt.ylabel("Marks")
#         plt.ylim(0,100)

#         plt.show()

#         print("\nStudent Added Successfully!")

#     elif choice == '3':  

#         cursor.execute("SELECT student_name, percentage, result FROM students_data")
#         data = cursor.fetchall()

#         if not data:
#             print("No student data found!")
#         else:
#             students = [row[0] for row in data]
#             percentages = [row[1] for row in data]
#             results = [row[2] for row in data]

#             import numpy as np
#             sorted_indices = np.argsort(percentages)[-3:]  # top 3
#             top3_indices = set(sorted_indices)

#             # Assign colors
#             colors = []
#             for i, res in enumerate(results):
#                 if res.lower() == "fail":
#                     colors.append('red')       # Fail students in red
#                 elif i in top3_indices:
#                     colors.append('gold')      # Top 3 in gold
#                 else:
#                     colors.append('skyblue')   # Others in blue

#             # Plot bar graph
#             import matplotlib.pyplot as plt
#             plt.figure(figsize=(12,6))
#             bars = plt.bar(students, percentages, color=colors)
#             plt.xlabel("Students")
#             plt.ylabel("Percentage")
#             plt.title("Student Percentage (Top 3 & Fail Highlighted)")
#             plt.xticks(rotation=45)
#             plt.ylim(0, 100)
#             plt.tight_layout()

#             for bar, pct in zip(bars, percentages):
#                 plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()+1, f"{pct:.1f}", ha='center', va='bottom')

#             plt.show()

#     elif choice == '4':
#         cursor.execute("SELECT result, COUNT(*) FROM students_data GROUP BY result")
#         data = cursor.fetchall()

#         if not data:
#             print("No student data found!")
#         else:
#             labels = [row[0] for row in data]   # Pass / Fail
#             counts = [row[1] for row in data]   # Number of students

#             colors = []
#             for label in labels:
#                 if label.lower() == "pass":
#                     colors.append("green")
#                 else:
#                     colors.append("red")

#             plt.figure(figsize=(6,6))
#             plt.pie(counts, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
#             plt.title("Pass vs Fail Students")
#             plt.axis("equal")

#             plt.show()

#     elif choice == '5':
#         cursor.execute("SELECT student_name, percentage FROM students_data")
#         data = cursor.fetchall()

#         if not data:
#             print("No student data found!")
#         else:
#             students = [row[0] for row in data]
#             percentages = [row[1] for row in data]

#             import numpy as np
#             top3 = np.argsort(percentages)[-3:]   # Top 3 students

#             colors = []
#             for i in range(len(percentages)):
#                 if i in top3:
#                     colors.append("gold")     # highlight topper
#                 else:
#                     colors.append("skyblue")

#             bars = plt.bar(students, percentages, color=colors)

#             plt.title("Student Percentage Comparison")
#             plt.xlabel("Students")
#             plt.ylabel("Percentage")
#             plt.xticks(rotation=45)
#             plt.ylim(0,100)

#             for bar, pct in zip(bars, percentages):
#                 plt.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f"{pct:.1f}", ha='center')

#             plt.show()


#     elif choice == '6':

#         cursor.execute("SELECT AVG(maths), AVG(science), AVG(english), AVG(social_science) FROM students_data")
#         data = cursor.fetchone()

#         if not data:
#             print("No data found!")
#         else:
#             subjects = ["Maths", "Science", "English", "Social Science"]
#             averages = [data[0], data[1], data[2], data[3]]

#             plt.bar(subjects, averages, color=["blue","green","orange","red"])

#             plt.title("Class Subject Average Marks")
#             plt.xlabel("Subjects")
#             plt.ylabel("Average Marks")
#             plt.ylim(0,100)

#             for i, avg in enumerate(averages):
#                 plt.text(i, avg+1, f"{avg:.1f}", ha='center')

#             plt.show()

#     elif choice == '7':

#         cursor.execute("SELECT grade, COUNT(*) FROM students_data GROUP BY grade")
#         data = cursor.fetchall()

#         if not data:
#             print("No student data found!")
#         else:
#             grades = [row[0] for row in data]
#             counts = [row[1] for row in data]

#             colors = {
#                 "A+": "gold",
#                 "A": "green",
#                 "B": "blue",
#                 "C": "orange",
#                 "D": "red"
#             }

#             bar_colors = [colors.get(g, "gray") for g in grades]

#             plt.figure(figsize=(8,5))
#             bars = plt.bar(grades, counts, color=bar_colors)

#             plt.title("Grade Distribution in Class")
#             plt.xlabel("Grades")
#             plt.ylabel("Number of Students")

#             for bar, count in zip(bars, counts):
#                 plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()+0.1,
#                         str(count), ha='center')

#             plt.show()

#     elif choice == '8':
#         start = input("Enter start student ID: ")
#         end = input("Enter end student ID: ")

#         while not start.isdigit() or not end.isdigit():
#             print("Enter valid numeric IDs")
#             start = input("Enter start student ID: ")
#             end = input("Enter end student ID: ")

#         start = int(start)
#         end = int(end)

#         cursor.execute(
#             "SELECT student_name, percentage, result FROM students_data WHERE student_id BETWEEN %s AND %s",
#             (start, end)
#         )

#         data = cursor.fetchall()

#         if not data:
#             print("No student data found in this range!")
#         else:
#             students = [row[0] for row in data]
#             percentages = [row[1] for row in data]
#             results = [row[2] for row in data]

#             import numpy as np

#             # Find top 3 percentages
#             top3 = np.argsort(percentages)[-3:]

#             colors = []
#             for i in range(len(percentages)):
#                 if results[i].lower() == "fail":
#                     colors.append("red")     # Fail students
#                 elif i in top3:
#                     colors.append("gold")    # Top 3
#                 else:
#                     colors.append("skyblue") # Others

#             plt.figure(figsize=(12,6))
#             bars = plt.bar(students, percentages, color=colors)

#             plt.title(f"Student Percentage Graph (ID {start} to {end})")
#             plt.xlabel("Students")
#             plt.ylabel("Percentage")
#             plt.xticks(rotation=90)
#             plt.ylim(0,100)

#             # Percentage label on bars
#             for bar, pct in zip(bars, percentages):
#                 plt.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1,
#                         f"{pct:.1f}", ha='center')

#             plt.tight_layout()
#             plt.show()

#     elif choice == '9':
#         print("Exiting program...")
#         break

#     else:
#         print("Invalid choice. Try again.")

# cursor.close()
# db.close()

import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_data"
)

cursor = conn.cursor()

while True:

    print("\n----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Percentage Graph (Top 5)")
    print("5. Grade Graph (All Students)")
    print("6. Total Marks Graph (Top 5)")
    print("7. Compare Subject Marks (Top 5)")
    print("8. Exit")

    choice = int(input("Enter your choice: "))


# ADD STUDENT
    if choice == 1:

        name = input("Enter Student Name: ")
        roll = int(input("Enter Roll No: "))
        gender = input("Enter Gender: ")

        maths = int(input("Enter Maths Marks: "))
        science = int(input("Enter Science Marks: "))
        english = int(input("Enter English Marks: "))
        social = int(input("Enter Social Science Marks: "))

        total = maths + science + english + social
        percentage = total / 4

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 35:
            grade = "D"
        else:
            grade = "F"

        result = "Pass" if percentage >= 35 else "Fail"

        sql = """INSERT INTO students
        (student_name, student_roll_no, gender, maths_marks, science_marks, english_marks, social_science_marks, total_marks, percentage, grade, result)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        values = (name, roll, gender, maths, science, english, social, total, percentage, grade, result)

        cursor.execute(sql, values)
        conn.commit()

        print("Student Added Successfully")


# VIEW STUDENTS
    elif choice == 2:

        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()

        for row in data:

            print("\nName:", row[1])
            print("Roll No:", row[2])
            print("Gender:", row[3])
            print("Maths:", row[4])
            print("Science:", row[5])
            print("English:", row[6])
            print("Social Science:", row[7])
            print("Total:", row[8])
            print("Percentage:", row[9])
            print("Grade:", row[10])
            print("Result:", row[11])


# DELETE STUDENT
    elif choice == 3:

        roll = int(input("Enter Roll No to Delete: "))

        sql = "DELETE FROM students WHERE student_roll_no=%s"
        cursor.execute(sql,(roll,))
        conn.commit()

        print("Student Deleted Successfully")


# PERCENTAGE GRAPH
    elif choice == 4:

        cursor.execute("SELECT student_name, percentage FROM students ORDER BY percentage DESC LIMIT 5")
        data = cursor.fetchall()

        names = []
        percentages = []

        for row in data:
            names.append(row[0])
            percentages.append(row[1])

        colors = []

        for i in range(len(percentages)):
            if i == 0:
                colors.append("red")
            elif i == 1:
                colors.append("orange")
            elif i == 2:
                colors.append("green")
            else:
                colors.append("blue")

        bars = plt.bar(names, percentages, color=colors)

        for bar,p in zip(bars,percentages):
            plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+1,f"{p:.1f}",ha='center')

        top1 = mpatches.Patch(color='red', label='Top 1')
        top2 = mpatches.Patch(color='orange', label='Top 2')
        top3 = mpatches.Patch(color='green', label='Top 3')
        others = mpatches.Patch(color='blue', label='Others')

        plt.legend(handles=[top1,top2,top3,others])

        plt.title("Top 5 Students Percentage")
        plt.xlabel("Student Name")
        plt.ylabel("Percentage")

        plt.show()


# GRADE GRAPH
    elif choice == 5:

        cursor.execute("SELECT grade, COUNT(*) FROM students GROUP BY grade")
        data = cursor.fetchall()

        grades = []
        counts = []

        for row in data:
            grades.append(row[0])
            counts.append(row[1])

        plt.pie(counts, labels=grades, autopct='%1.1f%%')

        plt.title("Grade Distribution")

        plt.legend(grades)

        plt.show()


# TOTAL MARKS GRAPH
    elif choice == 6:

        cursor.execute("SELECT student_name, total_marks FROM students ORDER BY total_marks DESC LIMIT 5")
        data = cursor.fetchall()

        names = []
        totals = []

        for row in data:
            names.append(row[0])
            totals.append(row[1])

        colors = []

        for i in range(len(totals)):
            if i == 0:
                colors.append("red")
            elif i == 1:
                colors.append("orange")
            elif i == 2:
                colors.append("green")
            else:
                colors.append("blue")

        bars = plt.bar(names, totals, color=colors)

        for bar,t in zip(bars,totals):
            plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+2,str(t),ha='center')

        top1 = mpatches.Patch(color='red', label='Top 1')
        top2 = mpatches.Patch(color='orange', label='Top 2')
        top3 = mpatches.Patch(color='green', label='Top 3')
        others = mpatches.Patch(color='blue', label='Others')

        plt.legend(handles=[top1,top2,top3,others])

        plt.title("Top 5 Students Total Marks")
        plt.xlabel("Student Name")
        plt.ylabel("Total Marks")

        plt.show()


# SUBJECT COMPARISON GRAPH
    elif choice == 7:

        cursor.execute("SELECT student_name, maths_marks, science_marks, english_marks, social_science_marks FROM students ORDER BY total_marks DESC LIMIT 5")
        data = cursor.fetchall()

        names = []
        maths = []
        science = []
        english = []
        social = []

        for row in data:

            names.append(row[0])
            maths.append(row[1])
            science.append(row[2])
            english.append(row[3])
            social.append(row[4])

        x = range(len(names))

        plt.plot(x, maths, marker='o', label="Maths")
        plt.plot(x, science, marker='o', label="Science")
        plt.plot(x, english, marker='o', label="English")
        plt.plot(x, social, marker='o', label="Social Science")

        plt.xticks(x,names)

        plt.title("Subject Marks Comparison")
        plt.xlabel("Student Name")
        plt.ylabel("Marks")

        plt.legend()

        plt.show()


# EXIT
    elif choice == 8:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")