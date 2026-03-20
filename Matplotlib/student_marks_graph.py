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
