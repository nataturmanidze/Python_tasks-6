import itertools

word = "ABCD"

variants = [''.join(p) for p in itertools.permutations(word)]

print("ყველა შესაძლო ვარიანტი:")
for variant in variants:
    print(variant)

total_count = len(variants)

print(f"სულ არის {total_count} ვარიანტი")