def get_initials():
    inp = input("Please insert full name: ")
    name_parts = inp.split()
    result = ''
    for part in name_parts:
        if part[0].isupper():
            result += part[0] + '.'
    print(result)

get_initials()
