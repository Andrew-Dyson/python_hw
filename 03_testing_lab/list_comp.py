# Remember, this effectively gives us a list of [1,2,3,4,5,6,7,8,9,10]
numbers = range(1, 11)
# evens_squared = []
# for number in numbers:
#     if number % 2 == 0:
#         evens_squared.append(number * number)

# print(evens_squared)

# evens_squared = [nums * nums for nums in numbers if nums % 2 == 0]
# Thing we want to return goes in the front, then the loop, the the if condition

# print(evens_squared)

# evens_squared = [number * number for number in range(1, 11) if number % 2 == 0]
# print(evens_squared)

# long way
ages = [5, 15, 64, 27, 84, 26]
odd_ages = []
for people in ages:
    if people % 2 == 1:
        odd_ages.append(people)
# short list way
odd_ages_new = [people for people in ages if people % 2 == 1]
# print(odd_ages_new)



chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
chicken_new = []
# long way
for names in chicken_names:
    if len(names) > 10:
        chicken_new.append(names)

# short list way
chicken_names_short = [chickens for chickens in chicken_names if len(chickens) > 10]

# print(chicken_new)
# print(chicken_names_short)

# long way
new_chick_list = []
for names in chicken_names:
    if names[0] == "H":
        new_chick_list.append(names)
print(new_chick_list)


words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]