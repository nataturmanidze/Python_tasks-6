from datetime import datetime, timedelta

today = datetime.now()

days_until_tuesday = (1 - today.weekday()) % 7

if days_until_tuesday <= 0 or today.weekday() >= 1:
    days_until_tuesday += 7
else:
    days_until_tuesday += 7

next_tuesday = today + timedelta(days=days_until_tuesday)

print(f"შემდეგი კვირის სამშაბათი იქნება: {next_tuesday.strftime('%A, %Y-%m-%d')}")