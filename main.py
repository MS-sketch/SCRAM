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

priority_level: It ranges from 1 to 5, with 1 being the highest priority and 5 being the lowest. It is
                generated automatically by the API, in accordance with the priority_level_dict.
                
activity_type: It can be 'study', 'work', 'exercise', 'activity', 'other'

deadline: It is the date when the task is due.

time_created: It is the time when the task is created. Auto Registered By API.

start_time: It is the time when the task is expected to start, given by user

"""


def main():
    pass


def priority(task_list, time_needed, priority_level, activity_type, time_created, deadline, start_time):
    pass


if __name__ == "__main__":
    main()
