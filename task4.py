from datetime import datetime

today = datetime.now()

next_year = today.year + 1
new_year = datetime(next_year, 1, 1)

days_left = (new_year - today).days

full_weeks = days_left // 7
remaining_days = days_left % 7

print(f"ახალ წლამდე დარჩენილია {full_weeks} კვირა და {remaining_days} დღე.")