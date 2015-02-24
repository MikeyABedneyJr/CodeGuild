def sleep_in(wd , vc):
		if wd == false and vc == false:
			return true
		elif wd == true and vc == false:
			return false
		elif wd == false and vc == true:
			return true

print "On weekdays, you wake up at 5:40am. If it is vacation, you wake up at 10am.\n Don't argue. We know this to be true..."
vacation = raw_input("Are you on vacation?\n>>>>> ")

weekday = raw_input("What day is it?\n>>>>> ")

if vacation.lower() in ["yes", "y", "ya", "yah"]:
	vacation = true
else:
	vacation = false

if weekday.lower() in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Mon", "Tues", "Wed", "Thurs", "Fri"]:
	weekday = true
else:
	weekday = false

sleep_in(weekday, vacation)

