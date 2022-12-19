
import datetime


date = datetime.datetime(2021 , 8, 10)
print(date.now().date())
print(date.strftime("%-b %d , %Y"))
print(date.strftime("%d - %-b - %Y"))
print(date.strftime("%d / %-b /%y"))
print(date.strftime("%d / %B / %Y"))
print(date.strftime("%a, %d %B %Y"))


# Today Is "2021, 8, 10"
"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"