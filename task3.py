import calendar

user_year = int(input("შეიყვანეთ წელი: "))

if calendar.isleap(user_year):
    print(f"{user_year} ნაკიანი წელია.")
else:
    print(f"{user_year} ნაკიანი წელი არ არის.")