# Author: Tow 2/9/21

def letter_frequency(string):
    letter_dict = {}
    for x in string:
        if x not in letter_dict:
            letter_dict[x.lower()] = 1
        elif x in letter_dict:
            letter_dict[x.lower()] += 1
    return


user_string = input("Enter astring: ")

frequency_table = letter_frequency(user_string)
del frequency_table[" "]

for key, value in sorted(frequency_table.items()):
    print(key, value)

