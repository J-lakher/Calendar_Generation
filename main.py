import calendar
year = int(input("enter year:")) #year
month = int(input("enter month:")) #month
calendar = calendar.month(year,month)
#display the calendar
print(calendar)