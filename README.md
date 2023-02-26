README

Introduction

This program is designed to find common availability between two people given their schedules and daily activities. The program takes the schedules and daily activities of both people as input, along with the duration of the meeting, and returns the available time slots when both people are free to meet.
Requirements

    Python 3.x

How to run the program

    To execute the program, follow these steps:

    Open a text editor or an integrated development environment (IDE) such as PyCharm or Visual Studio Code.
    Copy and paste the code into a new file, and save the file with a .py extension.
    Make sure you have Python 3 installed on your computer. If not, download and install it from the official website: https://www.python.org/downloads/
    Open a command prompt or terminal window and navigate to the directory where the Python file is saved.
    Run the program by typing python filename.py in the command prompt or terminal window, where filename is the name of the file you saved in step 2.
    Press enter to execute the program.
    The output of the program will be displayed in the console.

Note: You will need to provide the input for the program within the code file itself, as there are no prompts or command-line arguments for input. Simply modify the sample input provided in the code and save the file before running the program.

    Clone the repository to your local machine
    Navigate to the directory where the file group_schedule_problem.py is located.
    Run the command python group_schedule_problem.py to execute the program.
    The program will output a list of available time slots in military time format.

Input format

The program takes the following inputs:

    person1_Schedule: a list of lists, where each inner list represents a time slot in the format ['start_time', 'end_time'], where both start_time and end_time are in the format '%H:%M' (e.g., '09:30' represents 9:30 AM). This list represents the schedule of the first person.
    person1_DailyAct: a list of two strings representing the start and end times of the first person's daily activities in the format '%H:%M'.
    person2_Schedule: a list of lists representing the schedule of the second person in the same format as person1_Schedule.
    person2_DailyAct: a list representing the daily activities of the second person in the same format as person1_DailyAct.
    duration_of_meeting: an integer representing the duration of the meeting in minutes.

Output format

The program outputs a list of available time slots in the same format as person1_Schedule and person2_Schedule. Each inner list represents a time slot in the format ['start_time', 'end_time'], where both start_time and end_time are in the format '%H:%M'.


Example usage


# Sample input
person1_Schedule =[['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_DailyAct = ['9:00', '19:00']
person2_Schedule = [['9:00', '10:30'], ['12:20', '14:30'], ['14:00', '15:00'], ['16:00', '17:00']]
person2_DailyAct = ['9:00', '18:30']
duration_of_meeting = 30

# Call the function and print the result
available_times = find_common_availability(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, duration_of_meeting)
print(available_times)

Expected output


[['10:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
