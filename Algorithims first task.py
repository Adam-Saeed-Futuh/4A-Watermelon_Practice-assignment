weight = int(input())

if weight < 1 or weight > 100:
    print("Invalid input")
elif weight % 2 == 0:
    if weight == 2:
        print("Impossible to give even numbers after dividing")
    else:
        print("Possible to give even numbers after dividing")
else:
    print("Impossible to give even numbers after dividing")

# Counting the number of possible ways to divide the watermelon
count = 0
combinations = set()
for i in range(1, weight):
    if i % 2 == 0 and (weight - i) % 2 == 0:
        combination = tuple(sorted([i, weight-i]))
        if combination not in combinations:
            count += 1
            combinations.add(combination)

print("There are " + str(count) + " possible ways to divide it.")
if count > 0:
    print("The combinations are:", [list(c) for c in combinations], "and vice-versa of the arranged pair.")
