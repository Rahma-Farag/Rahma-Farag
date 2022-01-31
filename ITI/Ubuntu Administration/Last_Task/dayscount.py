import sys
from datetime import date

def getdays(uday, umonth, uyear):
  startdate = date(1970, 1 , 1 )
  userdate = date(uyear, umonth, uday)
  return userdate - startdate
 
 
args = sys.argv
if len(args) == 4:
	uday = int(args[1])
	umonth = int(args[2])
	uyear = int(args[3])
	days = getdays( uday, umonth, uyear)
else:
	print("please enter: day month year")
	uday, umonth, uyear = input().split(" ")
	days = getdays(int(uday), int(umonth), int(uyear))
	
	

print("The number of days is: ", days) 
