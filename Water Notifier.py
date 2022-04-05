import datetime
import time
from win10toast import ToastNotifier
def TimeInput():
	hrs = int(input("interval Hours\n"))
	mins = int(input("interval Mins\n"))
	time_interval = (mins*60)+(hrs*3600)
	return time
def notification():
	notification = ToastNotifier()
	notification.show_toast("Drink Water")

def notifyNow(time):
	while True:
		time.sleep(time)
		notification()
notifyNow()