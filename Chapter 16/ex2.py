import datetime
import calendar
import copy

def print_current_date_day():
	current_date = datetime.date.today()
	day_names = list(calendar.day_name)
	print("Today's date is:", current_date.isoformat())
	# Current day name as integer
	n = current_date.weekday()
	print('The weekday is:' , day_names[n])

def sec_to_time(seconds):
	""" Converts seconds into a corresponding time consisting of hours, minutes, and seconds
		Returns a tuple in the above order
	"""
	minutes, second = divmod(seconds, 60)
	hour, minute = divmod(minutes, 60)
	return hour, minute, second

def birthday_countdown():
	# user_bday = input('Please type your birthday in the format DDMMYYYY:')
	# actual day of birth
	user_bday = '07091986'
	birthday = datetime.datetime.strptime(user_bday, '%d%m%Y')
	today = datetime.datetime.now()
	print('Your birthday is', birthday.strftime('%d %B %Y'))
	# Note the below If statement which may adjust this variable
	age = today.year - birthday.year
	# birthday for the current year
	next_birthday = birthday.replace(year=today.year)
	if next_birthday < today:
		# if the birthday has already occurred this year, we want to check next year's (otherwise we get the time since the last birthday and not a countdown)
		next_birthday = next_birthday.replace(year=today.year + 1)
	else:
		# birthday hasn't happened yet which affects the age calculation
		age -= 1
	print('Your age is', age)
	# timedelta object
	countdown = next_birthday - today
	hour, minute, second = sec_to_time(countdown.seconds)
	print('Your next birthday is in', countdown.days, 'days,', hour, 'hours,', minute, 'minutes, and', second, 'seconds.' )

def find_age(dob, when='now'):
	""" dob = date of birth as a datetime object
		when = when to start cacluating the age, defaults to 'now'; can take a datetime object to work out what a person's age was/could be at set dates
	"""
	birthday = copy.copy(dob)
	if when == 'now':
		# age is based on current datetime
		today = datetime.datetime.now()
	else:
		# age is based on the caller's specified datetime (could be past or future)
		today = when
	age = today.year - birthday.year
	# birthday for the current year
	next_birthday = birthday.replace(year=today.year)
	if next_birthday > today:
		# birthday hasn't happened yet which affects the age calculation
		age -= 1
	return age

def double_day(person1, person2, n):
	dob1 = datetime.datetime.strptime(person1, '%d%m%Y')
	dob2 = datetime.datetime.strptime(person2, '%d%m%Y')
	# person1 must always be older than person2 in order to find the double day
	if dob1 > dob2:
		# swap the datetime objects around so that person1 is the oldest
		dob1, dob2 = dob2, dob1
	today = datetime.datetime.now()
	# work out how old person 1 is on person 2's actual birth date
	days_old_at_birth = dob2 - dob1
	res = dob2 + days_old_at_birth / (n - 1)
	return res
	

n = 2
my_double_day = double_day('20051984', '21052017', n).strftime('%d %B %Y')
print('Person 1 is', n, 'times older than Person 2 on', my_double_day)