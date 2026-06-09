import random
from datetime import datetime

secret_number = random.randint(1, 20)

start_time = datetime.now()

user_info = input("შეიყვანეთ რიცხვი: ")

end_time = datetime.now()
time_taken = (end_time - start_time).total_seconds()

if time_taken > 5.0:
    print("დრო ამოგეწურათ, თქვენ დამარცხდით!")
else:
    try:
        player_guess = int(user_info)
        if player_guess == secret_number:
            print("თქვენ გამოიცანით რიცხვი და ჩაეტიეთ დროში!")
        else:
            print("თქვენ ვერ გამოიცანით რიცხვი!")
    except ValueError:
        print("რიცხვი არ არის ვალიდური")