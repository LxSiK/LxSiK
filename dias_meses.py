def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "y"
      else:
        return "n"
    else:
      return "y"
  else:
    return "n"


def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == "y":
    month_days[1] += 1
  days = month_days[(month - 1)]
  return days


year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)