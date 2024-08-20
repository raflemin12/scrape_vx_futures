import calendar
# from datetime import strftime

years = [year for year in range(2013, 2026)]
months = [month for month in range(1,13)]

c = calendar.Calendar()

third_wed = []

for year in years:
    for month in months:
        third_wed.append([day.strftime('%Y-%m-%d') for week in c.monthdatescalendar(year,month) \
                          for day in week if day.weekday() == calendar.WEDNESDAY \
                          and day.month == month][2])

print(third_wed)