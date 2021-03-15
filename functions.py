tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasks
print('Uncompleted Tasks...')
def print_tasks_by_status(list, task_status):
    for task in tasks:
        if task['completed'] == task_status:
            print(task)
print_tasks_by_status(tasks, False)


# Print a list of completed tasks
print('Completed Tasks...')
def print_tasks_by_status(list, task_status):
    for task in tasks:
        if task['completed'] == task_status:
            print(task)
print_tasks_by_status(tasks, True)


# Print a list of all task descriptions
print('Task Descriptions...')
def print_task_descriptions(list):
    for task in tasks:
            print(task['description'])
print_task_descriptions(tasks)


# Print a list of tasks where time_taken is at least a given time
print('Task Timings...')
def print_tasks_by_time_taken(list, time):
    for task in tasks:
        if task['time_taken'] >= time:
            print(task)
print_tasks_by_time_taken(tasks, 30)


# Print any task with a given description
print('Described Task ...')
def print_tasks_by_description(list, description_requested):
    for task in tasks:
        if task['description'] == description_requested:
            print(task)
print_tasks_by_description(tasks, "Feed Cat")

# Extension
# Given a description update that task to mark it as complete.
print('Updating Tasks...')
def unpdate_task_by_descriptions(list, task_description):
    for task in tasks:
        if task['description'] == task_description:
           (task['completed']) = True
unpdate_task_by_descriptions(tasks, "Feed Cat")
print_tasks_by_description(tasks, "Feed Cat")

# Add a task to the list
print('Adding a Task ...')
def adding_task():
    description = input('Enter Task Description: ')
    time_taken = int(input("Enter Time Taken: "))
    new_task = {'description': description , 'completed': False, 'time_taken': time_taken}
    tasks.append(new_task)
    print(new_task)
adding_task()
print(tasks)


# Further Extensions
# Use a while loop to display the following menu and allow the use to enter an option.
# print("Menu:")
# print("1: Display All Tasks")
# print("2: Display Uncompleted Tasks")
# print("3: Display Completed Tasks")
# print("4: Mark Task as Complete")
# print("5: Get Tasks Which Take Longer Than a Given Time")
# print("6: Find Task by Description")
# print("7: Add a new Task to list")
# print("M or m: Display this menu")
# print("Q or q: Quit")
# Call the appropriate function depending on the users choice.