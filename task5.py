import itertools

my_list = [1, 2, 3, 4, 5]

all_combinations = list(itertools.combinations(my_list, 3))

for combo in all_combinations:
    print(combo)