def Grades():
    # 1. Variables MUST be initialized OUTSIDE the loop
    Student_count = 0
    Total_marks = 0
   while True:
        Grades_input = int(input("Enter marks (-1 to stop): "))
        
        # Sentinel Check: Program stops when user enters -1
        if Grades_input == -1:
            break
# Range Check Validation
        if 0 <= Grades_input <= 100:
            if Grades_input >= 80:
                print("Grade: A")
            elif Grades_input >= 70:
                print("Grade: B")
            elif Grades_input >= 60:
                print("Grade: C")
            else:
                print("Grade: F")
