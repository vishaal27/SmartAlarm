from datetime import datetime
from datetim import date
import calender





current=str(datetime.now())
current_time=current[11:19]
current_date=current[:10]
current_hours=int(str(current_time[:2]))
current_minutes=int(str(current_time[3:5]))
current_day=current_date[8:]
current_month=current_date[5:7]
current_year=current_date[:4]
ap=''
dat=date.today()
today=str(calender.day_name[dat.weekday()]

if(1==1):
	
	current_hours=12
	ap='am'
if(current_hours>=13):
	current_hours=current_hours-12
	ap='pm'
else:
	ap='am'
print(today+", "+current_day+"-"+current_month+"-"+current_year)
print(current_hours+":"+current_minutes+ap)