class clockTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def setHours(self, hours): 
        self.hours = hours
    def setMinutes(self, minutes): 
        self.minutes = minutes
    def setSeconds(self, seconds):
        self.seconds = seconds
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def showTime(self):
        print("Time: "+str(self.hours)+":"+str(self.minutes)+":"+str(self.seconds))

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if(hours>24 or hours < 0):
    print("Hours must be within 24 hr format")
elif(minutes>60 or minutes<0):
    print("Minutes must be within 0-60")
elif(seconds>60 or seconds<0):
    print("Seconds must be within 0-60")
else:
    clock = clockTime(hours, minutes, seconds)
    clock.showTime()