print("[[   My CGPA Calculator    ]]\nPlease enter '-1' during the first prompt of the pair of input prompts to exit after all desired inputs are entered.")

flag = False

while not flag:
    c_weight = 0
    c_points = 0

    while True:
        weight = float(input("\nEnter course weight: "))
        while weight != -1 and weight < 0:
            weight = float(input("\nERROR - Enter valid course weight: "))
        if weight == -1:
            break
        else:
            grade = float(input("Enter your grade point: "))
            while grade < 0:
                grade = float(input("ERROR - Enter valid grade point: "))
            c_points += (weight * grade)
            c_weight += weight
    if c_points != 0 and c_weight != 0:
        print(f'\nYour CGPA is {(c_points/c_weight):.2}.')

    if input("\nPress '1' to exit program, or anything else to restart program:  ") == "1":
        exit()
