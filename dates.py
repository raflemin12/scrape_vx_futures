import calendar

def third_wed_month(start_year: int, end_year: int) -> list:
    """
    Returns the third Wednesday of every month given a range of years
    """

    calendar_obj = calendar.Calendar()

    third_wed = []

    for year in range(start_year, end_year + 1):
        for month in range(1,13):
            third_wed.append([day.strftime('%Y-%m-%d') \
                          for week in calendar_obj.monthdatescalendar(year,month) \
                          for day in week if day.weekday() == calendar.WEDNESDAY \
                          and day.month == month][2])
    return third_wed
