import itertools
import random

numbers = [1, 2, 3, 4, 5, 6]

secret_password = random.choices(numbers, k=4)

secret_str = ""
for num in secret_password:
    secret_str += str(num)

all_combinations = itertools.product(numbers, repeat=4)

for attempt in all_combinations:
    attempt_str = "".join([str(num) for num in attempt])
    
    print(f"დაცდილი პაროლი: {attempt_str}")
    if list(attempt) == secret_password:
        print(f"გილოცავთ თქვენი შეყვანილი პაროლი: {attempt_str} სწორია!")
        break