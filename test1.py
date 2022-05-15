def most_wanted_letter(string):
    max_num = 0
    most_wanted = 0
    string = string.lower()
    alpha = None
    for i in range(len(string)):
        num = 0
        if not string[i].isalpha():
            continue
        alpha = 1
        for j in range(len(string)):
            if not string[j].isalpha() or i == j:
                continue
            if string[i] == string[j]:
                num += 1
        if num >= max_num:
            max_num = num
            most_wanted = string[i]
    if not alpha:
        return "There are no letters in the string."
    else:
        return f"The most popular letter is {most_wanted}"


print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))



