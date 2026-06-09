import random
from datetime import datetime, timedelta

start = datetime.now()

player1_finish = start + timedelta(seconds=random.randint(5, 20))
player2_finish = start + timedelta(seconds=random.randint(5, 20))

if player1_finish < player2_finish:
    print("გამარჯვებულია პირველი მოთამაშე!")
    
elif player2_finish < player1_finish:
    print("გამარჯვებულია მეორე მოთამაშე!")    
else:
    print("ნიჩიაა!")