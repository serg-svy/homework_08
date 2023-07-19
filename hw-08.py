import datetime

def get_birthdays_per_week(users):
  Args:
  Returns:
  today = datetime.date.today()
  week_ahead = today + datetime.timedelta(days=7)
  birthdays_per_week = {}
  for user in users:
    birthday = user['birthday']
    if birthday >= today and birthday < week_ahead:
      day_of_week = birthday.weekday()
      if day_of_week in birthdays_per_week:
        birthdays_per_week[day_of_week].append(user['name'])
      else:
        birthdays_per_week[day_of_week] = [user['name']]

  for day_of_week, users in birthdays_per_week.items():
    print(f'{day_of_week}: {", ".join(users)}')


if __name__ == '__main__':
  users = [
    {'name': 'Bill', 'birthday': datetime.date(1980, 1, 1)},
    {'name': 'Jill', 'birthday': datetime.date(1981, 2, 2)},
    {'name': 'Kim', 'birthday': datetime.date(1982, 3, 3)},
    {'name': 'Jan', 'birthday': datetime.date(1983, 4, 4)},
  ]
  get_birthdays_per_week(users)

