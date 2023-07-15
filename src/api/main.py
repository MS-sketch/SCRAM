# SCRAM : SCHEDULER ANALYTICS MANAGER
"""
AIM : THIS IS A SCHEDULE MANAGEMENT SOFTWARE API, INTENDED TO BE ONLY USED AT THE USER'S CHOICE.
THIS IS A SIMPLE API THAT ALLOWS THE USER TO MANAGE THE SCHEDULE OF A SPECIFIC STUDENT.
THE API HAS TWO MAIN FUNCTIONS:
1. CREATE A SCHEDULE
2. VIEW A SCHEDULE
3. EDIT A SCHEDULE
4. DELETE A SCHEDULE
5. SEARCH A SCHEDULE
6. CHECK A SCHEDULE AS MARKED
7. CHECK A SCHEDULE AS UNMARKED
8. SET DEADLINE FOR A SCHEDULE
9. AUTO SET PRIORITY OF WHAT SHOULD BE DONE BASED ON PARAMETERS PROVIDED BY THE USER.
10. STORE ALL IN A DB.
"""

"""
task_list: list of tasks.

priority_level_dict: dictionary of priority levels.

priority_level: It ranges from 1 to 5, with 1 being the lowest priority and 5 being the highest. It is
                generated automatically by the API, in accordance with the priority_level_dict.
                There can only be 3 level 5 priority tasks.
                
activity_type: It can be 'study', 'work', 'exercise', 'activity', 'other'
                The values are:
                Study =  5
                Work =  4
                Exercise =  3
                Activity =  2
                Other =  1

deadline: It is the date when the task is due. Value [1, 2, 3, 4, >5] days from the current date.
          With 1 day = 5 [IMP]
          >5 = 1 [Least IMP]

time_created: It is the time when the task is created. Auto Registered By API.

start_time: It is the time when the task is expected to start, given by user

time_needed: It is the time needed to complete the task. Estimate given by user, & 30 minutes is added as buffer.
            Ranges from levels 1 to 10. These are so as to arrange the tasks in accordance to the time
            available, Smallest on Top & Longest at last. It will warn the user a day or 2 before deadline.

"""

"""
Calculating priority is as follows & are done by priority_level_dict:
(activity_type + deadline)/2 = priority_level

"""


# Variables Are set

task_list = []

# Functions Are Defined


def main():
    pass


def priority(task_list, time_needed, priority_level, activity_type, time_created, deadline_date, deadline_time,
             start_time):
    # Count Number of items in task_list
    task_count = len(task_list)

    # Calculating Deadline
    deadline = deadline_calculation(deadline_date, deadline_time)

    # For Every Item find the priority_level
    for i in range(task_count):
        priority_level_dict(activity_type, deadline)

    pass


def priority_level_dict(activity_type, deadline):

    match  activity_type:
        case 'study':
            activityValue = 5
        case 'work':
            activityValue = 4
        case 'exercise':
            activityValue = 3
        case 'activity':
            activityValue = 2
        case 'other':
            activityValue = 1

    return (activityValue + deadline)/2


def deadline_calculation(deadline_date, deadline_time):
    return 0


def db_handler():
    pass


if __name__ == "__main__":
    main()
