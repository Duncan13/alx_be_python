task = input('Enter your task: ')
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print('The task is not time bound')
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}'  is a medium priority that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print('The task is not time bound')
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a low priority that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print('The task is not time bound')
    case _:
        print('Invalid priority level')
