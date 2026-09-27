for x in range(1,4):
    print("Student", x)
    Student = input("Enter Student Name: ")
    Activity_1 = int(input("Enter Activity 1  : "))
    Activity_2 = int(input("Enter Activity 2  : "))
    Activity_3 = int(input("Enter Activity 3  : "))
    print()

    #Calculates the Sum of Activity 1, 2, and 3 and Average of Score
    total = Activity_1 + Activity_2 + Activity_3
    score = total / 3
    print("Average:", score)

    #Will define the student's score status
    def average(score):
        if score >= 90:
            return("Excellent")
        elif score >= 80:
            return("Very Good")
        elif score >= 75:
            return("Passed")
        else:
            return("Failed")

    ave_score = average(score)

    print("Status :", ave_score)
    print()