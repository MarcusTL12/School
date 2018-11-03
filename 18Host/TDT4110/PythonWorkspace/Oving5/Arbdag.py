import ConsoleUtil as cu


WEEK = (
	"man",
	"tir",
	"ons",
	"tor",
	"fre",
	"lør",
	"søn"
)


def is_leap_year(year):
	return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def weekday_newyear(year):
	year -= 1
	return (year + year // 4 - year // 100 + year // 400) % 7


def is_workday(day):
	return day < 5


def workdays_in_year(year):
	weekday = weekday_newyear(year)
	return 260 + (1 if is_workday(weekday) else 0) + (1 if is_leap_year(year) and is_workday((weekday + 1) % 7) else 0)


def a():
	for i in range(1900, 1920):
		print(str(i) + " " + WEEK[weekday_newyear(i)])


def b():
	print(is_workday(2))
	print(is_workday(5))


def c():
	for i in range(1900, 1920):
		print(str(i) + " har " + str(workdays_in_year(i)) + " arbeidsdager")
