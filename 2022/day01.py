# Read the data, and split by empty lines, to return a list.
# Each element in the list is a single str, containing all the meal calorie values for that elf. Each calorie value is separated by a single newline character. (Because all the calorie values were on separate lines.)
# Split this str into its constituent numbers, by using splitlines(). Each calorie value is returned as a str.
# Convert every number str to an int. The Pythonic way to do this is using the map() function.
# Sum these numbers. This gives us the total calorie count for each elf. Add this count to a list.
# Finally, use max() to return the biggest number in our list.

with open('2022/input_files/day01.txt', 'r') as f:
    elf_meals = f.read().split("\n\n") # split on empty lines

elf_calories = [] # store total calories for each elf
for elf in elf_meals:
    calories = sum(map(int, elf.splitlines()))
    elf_calories.append(calories)
elf_calories = sorted(elf_calories)
print(sum(elf_calories[-3:]))
