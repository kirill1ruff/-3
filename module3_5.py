def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 0:
        return 1
    if len(str_number) == 1:
        return int(str_number[0]) if str_number[0] != '0' else 1
    first_digit = int(str_number[0])
    if first_digit != 0:
        return first_digit * get_multiplied_digits(int(str_number[1:]))
    else:
        return get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)  