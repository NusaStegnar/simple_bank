from datetime import date

dt = date.today()
print(dt)

year = dt.year
month = dt.strftime("%B")
day = dt.day
print(year, month, day)


year = 48

date_year = date((dt.month)  + year)
print(date_year)