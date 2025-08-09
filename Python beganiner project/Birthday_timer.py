# what i want to do
# i want to make a program which will take our date of birth and run a timer 
# until my next birthay
import time
from datetime import datetime,timedelta
name= input("Enter your name: ").capitalize()
genders= input("Enter your Gender: ").capitalize()
month_count=0

while True:
    if genders== "Male":
      print(f"Welcome Mr.{name}")
      break
    elif genders== "Female":
      print(f"Welcome Mrs.{name}")
      break
    elif genders== "Other,s":
      print(f"Welcome {name}")
      break
    else:
       print("Enter valid option (male,female,other,s)")
       genders= input("Enter your Gender: ").capitalize()
date=int(input("Enter your born date: ") )  
month=input("Enter your born month: ").capitalize()
while True:
   if month=="January":
      month_count=1
      break
   elif month== "February":
        month_count=2
        break
   elif month== "March":
        month_count=3
        break
   elif month== "April":
        month_count=4
        break
   elif month== "May":
        month_count=5
        break
   elif month== "June":
       month_count=6
       break
   elif month== "July":
       month_count=7
       break
   elif month== "Auguest":
       month_count=8
       break
   elif month== "September":
      month_count=9 
      break
   elif month== "October":
       month_count=10
       break
   elif month== "November":
      month_count=11 
      break
   elif month== "December":
      month_count=12
      break
   else:
      print("Invalid entry")
      month=input("Enter your born month: ").capitalize()
      
          
year=int(input("Enter your born year: ") )
print()
print(f"You D.O.B is {date}-{month}-{year}")
dob= datetime(year,month_count,date)
now=datetime.now()
this_year_birthday=datetime(now.year,month_count,date)
if this_year_birthday<now:
    next_year_birthday=datetime(now.year+1,month_count,date)
else:
    next_year_birthday= this_year_birthday
print("Your next birthday is on:",next_year_birthday.strftime("%d-%m-%Y"))
while True:
  now=datetime.now()
  left_time= next_year_birthday-now
  total_second_left= int(left_time.total_seconds())
  if total_second_left<=0:
      print("------HAPPY BIRTHDAY-----")
      print("------Dear {name} -------")
      break
  day,rem= divmod(total_second_left,86400)
  hours,rem=divmod(rem,3600)
  minute,rem= divmod(rem,60)
  second=rem
  print(f"Time left: {day} day {hours:02}:{minute:02}:{second:02}")
  time.sleep(1)
