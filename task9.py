from datetime import date

today = date.today()

try:
    birth_year = int(input("შეიყვანეთ დაბადების წელი: "))
    birth_month = int(input("შეიყვანეთ დაბადების თვე: "))
    birth_day = int(input("შეიყვანეთ დაბადების რიცხვი: "))
    
    birthday = date(birth_year, birth_month, birth_day)
    
except ValueError:
    print("\nშეიყვანეთ მოცემული მონაცემები!")
    exit()

next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_left = (next_birthday - today).days


if days_left == 0:
    print("გილოცავთ დაბადების დღეს!")
else:
    print(f"თქვენ დაბადების დღემდე დარჩენილია {days_left} დღე!")