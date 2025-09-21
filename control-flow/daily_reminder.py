task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no)")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a {priority} task that requires immediate attention today")
        else:
            print(f"{task} is a {priority} task. Consider completing it when you have free time")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a {priority} task that requires some attention today")
        else:
            print(f"{task} is a {priority} task. Consider completing it when you have free time")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a {priority} task that can be completed some time today")
        else:
            print(f"{task} is a {priority} task. Consider completing it when you have free time")