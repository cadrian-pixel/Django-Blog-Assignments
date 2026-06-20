# Conner Adrian
# The name of the app will be GPA Qualifier, or GPAQ for short
# This app is meant to determine GPA scores based on student name
# LNAME = Student's last name, FNAME = Student's first name, GRADE = Student's GPA
try:
    LNAME = str(input("Please enter the student's last name:"))
    FNAME = str(input("Please enter the student's first name:"))
    GRADE = float(input("Please enter the student's GPA:"))
    while LNAME != "ZZZ":
        if not LNAME.isalpha() or not FNAME.isalpha():
            raise ValueError("That is not a valid name.")
        if GRADE >= 3.5:
            print(f"{FNAME} {LNAME} has made the Dean's List!")
            LNAME = str(input("Please enter the student's last name:"))
            if LNAME == "ZZZ":
                break
            FNAME = str(input("Please enter the student's first name:"))
            GRADE = float(input("Please enter the student's GPA:"))
        elif GRADE >= 3.25:
            print(f"{FNAME} {LNAME} has made the Honor Roll!")
            LNAME = str(input("Please enter the student's last name:"))
            if LNAME == "ZZZ":
                break
            FNAME = str(input("Please enter the student's first name:"))
            GRADE = float(input("Please enter the student's GPA:"))
except ValueError:
    print("That entry is not valid. Restart application.")