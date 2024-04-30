from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events, request_user):
		events_per_day = events.filter(event_date__day=day, users_event_id=request_user.id)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events, request_user):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events, request_user)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, request_user, withyear=True):
		events = Event.objects.filter(event_date__year=self.year, event_date__month=self.month, users_event_id=request_user.id)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events, request_user)}\n'
		return cal