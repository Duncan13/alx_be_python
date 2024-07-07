from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  print(f'Current date and time: {datetime.strftime(current_date, "%Y-%m-%d %H:%M:%S")}')

d1 = int(input('Enter the number of days to add to the current date: '))

def calculate_future_date(d1):
  current_date = datetime.now()
  future_date = current_date + timedelta(days = d1)
  print(f'Future date: {datetime.strftime(future_date, "%Y-%m-%d")}')
