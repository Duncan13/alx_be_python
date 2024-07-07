from _datetime import datetime, timedelta

current_date = datetime.now()
print(f'Current date and time: {current_date}')

d1 = int(input('Enter the number of days to add to the current date: '))

def calculate_future_date(d1):
  future_date = current_date + timedelta(days = d1)
  print(f'Future date: {datetime.strftime(future_date, "%Y-%m-%d")}')
