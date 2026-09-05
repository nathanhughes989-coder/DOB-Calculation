# Importing calendar module
import calendar

# To take month and year input from the user
year = int(input("Enter year: "))
month = int(input("Enter month, between 1-12: "))

# Display the calendar
print(calendar.month(year, month))