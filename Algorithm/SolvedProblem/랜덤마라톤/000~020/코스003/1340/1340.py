import datetime, calendar
date = datetime.datetime.strptime(input(), "%B %d, %Y %H:%M")
divFact = 5256
if calendar.isleap(date.year):
    divFact += 60 * 24 / 100
print((((date.toordinal() - date.replace(month=1, day=1, hour=0, minute=0).toordinal()) * 24 + date.hour) * 60 + date.minute) / divFact)
