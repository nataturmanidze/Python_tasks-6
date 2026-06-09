import itertools

word = "XYZ"

for length in range(1, 4):
    combos = itertools.combinations(word, length)
    for c in combos:
        clean_string = "".join(c)
        print(clean_string)