import pandas as pd 
import nfl_data_py as nfl   
from heplerFunctions import get-team-records
schdeule = nfl.import_schedules([2020, 2021, 2022])

print(schdeule.colums.tolist())

import pandas as pd
import nfl_data_py as nfl   

# Load the schedule data for the years 2020, 2021, and 2022
schedule = nfl.import_schedules([2020, 2021, 2022])
print(schedule.columns.tolist())
# Display the first few rows of the schedule DataFrame
print(schedule.head())
# Display the first few rows of the schedule DataFrame
print(schedule.head())


 while number != 'stop':
    number = input("Enter a number to square (or 'stop' to end): ")
    if number != 'stop':
        try:
            num = float(number)
            print(f"The square of {num} is {num ** 2}")
        except ValueError:
            print("Please enter a valid number.")

s.print(schedule.head())
print(schdeule.head())
print(schdeule.colums.tolist())
print(schdeule.head())
print(schdeule.head())


else:
schedules = nfl.import_schedules([2024])head()

 # For loop
 # Add team records to the schedule DataFrame
schedule_with_records = get_team_records(schedule)