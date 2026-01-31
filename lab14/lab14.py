from datetime import datetime, timedelta
import time

# Exercise 1
now = datetime.now()
string = now.strftime("%d-%m-%Y %H:%M:%S")
print(string)

# Exercise 2
current = datetime.now()
new_year = datetime(current.year,12, 31)

if current > new_year:
    new_year = datetime(current.year + 1,12,31)

remaining = new_year - current
print("Remaining days until New Year's Eve:", remaining.days)

# Exercise 3
sec = int(input("Please insert seconds for countdown: "))

def countdown(seconds):
    while seconds:
        print("Remaining time:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1
    print("Time is up!")

countdown(sec)

# Exercise 4
chosen_month = int(input("Please insert the number of the month: "))
chosen_year = int(input("Please insert the year: "))

def calendar(month, year):
    current_date = datetime(year, month, 1)
    start_weekday = current_date.weekday()

    if  month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)

    last_day = next_month - timedelta(days=1)

    print("Mon Tue Wed Thu Fri Sat Sun")
    print("    " * start_weekday, end="")

    while current_date <= last_day:
        print(f"{current_date.day:3}", end=" ")

        if current_date.weekday() == 6:
            print()

        current_date += timedelta(days=1)
    print()

calendar(chosen_month, chosen_year)