# Calender-Management-System
For my high school final project, I designed and developed an efficient Python calendar management software, harnessing the power of Python's def functions and seamlessly integrating a MySQL database.

## Introduction:
This project is all about software for the Calendar management system. It helps to manage the calendar between teachers and students.

## Requirements:
* Python 3.x
* MySQL

## About the System:

### 1) Aim:
To take schedules or time tables of two people (teacher and student) and manage it to find the time during which both the parties would be available for a meeting by seeing the time occupied and taking in considerations the daily bounds


### 2) Plan For Implementation:
This is a 2-user input program. The teacher and student will input their respective time tables and the program will display the time slots in which both of them are free. This time slot would depend on the option selected by the student for example 5 minutes for a doubt, 2 minutes for general query and 45 minutes to an hour for any conceptual problem. The teacher would have the authorization to add, delete and change slots. 


### 3) Type of Data:
* MySQL Database


TEACHER’S TABLE:
_________________________________________________________________________
|   | Data Items     | Type of Data | Description                        |                                                               _________________________________________________________________________
| 1 | S.No           | INT          | The serial number in the table.    |
| 2 | Teacher Name   |VARCHAR       | To enter the teacher's name.       |
| 3 | Time Available |VARCHAR       | To enter the time teacher is free. |
__________________________________________________________________________

Example of Tabular Representation of Data :

| S.No | NAME OF TEACHER | TIME BOOKED                                  | 
| 1    | Mohitendra Dey  | 8:00-8:30,9:30-10:45,11:00-11:30,12:00-12:45 | 
| 2    | ...             |...                                           | 
| 3    | ...             |...                                           | 



STUDENT’S TABLE:

|   | Data Items     | Type of Data | Description                        |
| 1 | S.No           | INT          | The serial number in the table.    |
| 2 | Student Name   |VARCHAR       | To enter the student's name.       |
| 3 | Time Available |VARCHAR       | To enter the time student is free. |


Example of Tabular Representation of Data :

| S.No | NAME OF STUDENT    | TIME BOOKED                                  | 
| 1    | Devyani Ghildiyal  | 8:10-8:40,9:00-10:55,11:00-11:30,12:10-12:55 | 
| 2    | ...                |...                                           | 
| 3    | ...                |...                                           | 


Menu Options

Teachers Information:

Main Menu
Sub Menu
Input       
i.   S.no 


ii. Name Of Teacher


iii. Time Available
Reports
i.Free time 



Students Information:

Main Menu
Sub Menu
Input 
i.  S.no


ii. Name of Student


iii. Time Available
Reports
i. Free time





### 4) Validation and Add on Features   
In case the user enters any wrong input, we will ask them to retry.The user can input data more than once in a single run and will have results accordingly.The database will be deleted once the whole code is told to quit. The coding will be user friendly and the users will find everything comfortable. 

## License
This project is licensed under the Creative Commons Zero v1.0 Universal license.

## Contact
For any questions regarding the project, you can reach out to:

* Project Creator: Devyani Ghildiyal
* Email: devyanighildiyal07@gmail.com
