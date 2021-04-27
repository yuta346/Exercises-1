#Completed

class Clock:
    def __init__(self,hrs,mins,secs):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hrs,self.mins,self.secs)

class Calendar:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.day,self.month,self.year)


class CalendarClock(Clock,Calendar):
    def __init__(self,day,month,year,hrs,mins,secs):
        Clock.__init__(self,hrs,mins,secs)
        Calendar.__init__(self,day,month,year)

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}, {3:02d}:{4:02d}:{5:02d}".format(self.day,self.month,self.year,self.hrs,self.mins,self.secs)

