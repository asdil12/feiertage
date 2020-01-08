#!/usr/bin/python3

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

from datetime import date, timedelta

def neujahr(year):
	return date(year, 1, 1)

def heilige_drei_koenige(year):
	return date(year, 1, 6)

def ostersonntag(year):
	"""
		 Butcher's Algorithm: Returns Easter as a date object.
	"""
	a = year % 19
	b = year // 100
	c = year % 100
	d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
	e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
	f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
	month = f // 31
	day = f % 31 + 1
	return date(year, month, day)

def karfreitag(year):
	return ostersonntag(year) - timedelta(days=2)

def ostermontag(year):
	return ostersonntag(year) + timedelta(days=1)

def tag_der_arbeit(year):
	return date(year, 5, 1)

def christi_himmelfahrt(year):
	return ostersonntag(year) + timedelta(days=39)

def pfingstmontag(year):
	return ostersonntag(year) + timedelta(days=50)

def fronleichnam(year):
	return ostersonntag(year) + timedelta(days=60)

def tag_der_deutschen_einheit(year):
	return date(year, 10, 3)

def allerheiligen(year):
	return date(year, 11, 1)

def heilig_abend(year):
	return date(year, 12, 24)

def erster_weihnachtsfeiertag(year):
	return date(year, 12, 25)

def zweiter_weihnachtsfeiertag(year):
	return date(year, 12, 26)

def silvester(year):
	return date(year, 12, 31)

def public_holidays(year):
	return [
		("Neujahr", neujahr(year)),
		("Heilige drei Könige", heilige_drei_koenige(year)),
		("Ostersonntag", ostersonntag(year)),
		("Karfreitag", karfreitag(year)),
		("Ostermontag", ostermontag(year)),
		("Tag der Arbeit", tag_der_arbeit(year)),
		("Christi Himmelfahrt", christi_himmelfahrt(year)),
		("Pfingstmontag", pfingstmontag(year)),
		("Fronleichnam", fronleichnam(year)),
		("Tag der deutschen Einheit", tag_der_deutschen_einheit(year)),
		("Allerheiligen", allerheiligen(year)),
		("Heilig Abend", heilig_abend(year)),
		("1. Weihnachtsfeiertag", erster_weihnachtsfeiertag(year)),
		("2. Weihnachtsfeiertag", zweiter_weihnachtsfeiertag(year)),
		("Silvester", silvester(year)),
	]

def ical(days):
	s = ""
	s += "BEGIN:VCALENDAR\n"
	s += "VERSION:2.0\n"
	s += "CALSCALE:GREGORIAN\n"
	s += "PRIDID:-//Feiertage////\n"
	s += "SUMMARY:Feiertage\n"
	s += "X-APPLE-CALENDAR-COLOR:#B027AE\n"
	for (name, d) in days:
		s += "BEGIN:VEVENT\n"
		s += "SUMMARY:%s\n" % name
		s += "DTSTART;VALUE=DATE:%s\n" % d.isoformat().replace('-', '')
		s += "DTEND;VALUE=DATE:%s\n" % (d+timedelta(days=1)).isoformat().replace('-', '')
		s += "UID:%s\n" % d.isoformat()
		s += "END:VEVENT\n"
	s += "END:VCALENDAR\n"
	return s


print("Content-Type: text/calendar;charset=UTF-8\n")
#print("Content-Type: text/plain;charset=UTF-8\n")
year = date.today().year
days = []
for y in range(year-10, year+10):
	days.extend(public_holidays(y))
print(ical(days))
