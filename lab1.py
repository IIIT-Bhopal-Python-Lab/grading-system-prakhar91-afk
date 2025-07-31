student_input="" #Initializing with dummy value

while student_input.upper() != "EXIT":
    student_input = input("Enter marks between 0 and 100 (or type 'EXIT' to quit): ")

    if  student_input.upper() == "EXIT":#If exit then stops the program
        print("Program Exiting.Bye!")
        break

    if not student_input.isdigit():#Cheking if input is valid number
        print("Enter a valid input between 0 and 100")
        continue

    marks=int(student_input)

    if marks <0 or marks > 100:#Checking if Value lies within the range
        print("Enter a valid input between 0 and 100")
        continue
#Now grading according to their marks with appropriate remarks
    if 90 <= marks <= 100:
        print("Outstanding, You got A")
    elif 75 <= marks <= 89:
        print("Excelent, You got B")
    elif 60 <= marks <= 74:
        print("Good, You got C")
    elif 40 <= marks <= 59:
        print("Could be better, You got D")
    else:
        print("Try Something Else, You got F")
