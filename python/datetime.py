>>> a = datetime.date(1998,12,14)
>>> a
datetime.date(1998, 12, 14)
>>> b = datetime.date.today()
>>> b
datetime.date(2020, 1, 14)

>>> a.ctime()
'Mon Dec 14 00:00:00 1998'
>>> a.isocalendar()
(1998, 51, 1) # Year | Week | Monday-Sunday (1-7)
>>> a.isoweekday()
1
>>> a.weekday()
0

d.replace([year [, month [, day ]]])
>>> a.replace(day = 13)
datetime.date(1998, 12, 13)



>>> a.toordinal()
729737
>>> c = datetime.date.fromordinal(729738)
>>> c
datetime.date(1998, 12, 15)
>>> a
datetime.date(1998, 12, 14)









>>> a = datetime.time(12,30,15,12)
>>> a
datetime.time(12, 30, 15, 12)
>>> a.isoformat()
'12:30:15.000012'


t.replace([hour [, minute [, second [, microsecond [, tzinfo ]]]]])
>>> a.replace(minute = 10)
datetime.time(12, 10, 15, 12)







>>> a = datetime.datetime(2020,1,15,20,20,20,10)
>>> a
datetime.datetime(2020, 1, 15, 20, 20, 20, 10)

datetime.combine(date,time)

>>> b = {
	"date": datetime.date(2020,1,15),
	"time": datetime.time(20,0,1,10)
}
>>> c = datetime.datetime.combine(b["date"],b["time"])
>>> c
datetime.datetime(2020, 1, 15, 20, 0, 1, 10)




>>> z = datetime.datetime.now()
>>> z
datetime.datetime(2020, 1, 14, 18, 7, 56, 731325)

>>> grinvich = datetime.datetime.utcnow()
>>> grinvich
datetime.datetime(2020, 1, 14, 16, 8, 39, 472651)



td = date1 - date2 # Повертає об'єкт timedelta
date2 = date1 + td # Добавляє різницю timedelta до об'єкту date
date2 = date1 - td # Віднімає різницю

# Порівняння
date1 < date2
date1 <= date2
date1 == date2
date1 != date2
date1 > date2
date1 >= date2

#! Не забувати про об'єкт часового поясу (якщо він присутній)



!timedelta
td3 = td2 + td1     # Додавання
td3 = td2 - td1     # Віднімання
td2 = i * td1       # Множення на int
td2 = td1 // i      # Цілочисельне ділення з округленням вниз
td2 = -td1          # Унарний мінус
td2 = +td1


# Порівняння
td1 < td2
td1 <= td2
td1 == td2
td1 != td2
td1 > td2
td1 >= td2

>>> today = datetime.datetime.now()
>>> today.ctime()
‘Thu Oct 20 11:10:10 2005’
>>> oneday = datetime.timedelta(days=1)
>>> tomorrow = today + oneday
>>> tomorrow.ctime()
‘Fri Oct 21 11:10:10 2005’
>>>



>>> s = "Aug 23, 2008"
>>> from datetime import datetime
>>> d = datetime.strptime(s, "%b %d, %Y")
>>> d
datetime.datetime(2008, 8, 23, 0, 0)


#!!!!!!!!!!!!!!!!!!!!!!!!!!
#! tzinfo клас (ст.428)
#!!!!!!!!!!!!!!!!!!!!!!!!!!