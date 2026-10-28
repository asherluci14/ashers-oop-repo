class DigitalClock:
    def __init__(self, pHr, pMin, pAm):
        self.hr = pHr
        self.min = pMin
        self.is_am = pAm

    def displayTime(self):
        am_pm = 'am' if self.is_am else 'pm'
        print(f"{self.hr}:{self.min}{am_pm}")

    def passTime(self, minutesPassed):
        self.min += minutesPassed

        self.hr += self.min // 60
        self.min = self.min % 60

        self.is_am = not self.is_am if (self.hr >= 12) else self.is_am

        self.displayTime()

clock1 = DigitalClock(11,59,True)

clock1.displayTime()
clock1.passTime(83)