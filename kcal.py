print("--WELCOME TO KCAL ANALYSIS--")
print("[1] MALE")
print("[2] FEMALE")
print("[3] EXIT")

user_choice = input("Enter your choice: ")
while user_choice in ['1', '2'] and user_choice != '3':
    try:
        weight = int(input("[KG] Enter your weight: "))
        height = int(input("[CM] Enter your height: "))
        age = int(input("[AGE] Enter your age: "))
        active = input(
            "[?] Enter your activity (Sedentary, Lightly, Moderately, Active, VeryActive): ").lower()

        if user_choice == '1':
            mbr_results = 66.47 + (13.75 * weight) + \
                (5.003 * height) - (6.755 * age)
        else:
            mbr_results = 655.1 + (9.563 * weight) + \
                (1.850 * height) - (4.676 * age)
        if active == 'sedentary':
            kcal_results = mbr_results * 1.2
        elif active == 'lightly':
            kcal_results = mbr_results * 1.375
        elif active == 'moderately':
            kcal_results = mbr_results * 1.55
        elif active == 'active':
            kcal_results = mbr_results * 1.725
        else:
            kcal_results = mbr_results * 1.9
        print("[KCAL] Daily Calories based on your info:", kcal_results)
        break
    except ValueError:
        print("Enter a valid number not a string.")
