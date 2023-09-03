# new_list = [new_item for item in items if test]

numbers = [1, 2, 3]
new_numbers = [item + 1 for item in numbers]

name = "Angela"
new_list = [letter for letter in name]
print(new_list)


new_range = [n * 2 for n in range(1, 5)]
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)
