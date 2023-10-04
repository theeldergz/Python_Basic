upper_sym = False
count_digit = 0
len_password = 0

while upper_sym == False or count_digit < 3 or len_password < 8:
    upper_sym = False
    count_digit = 0
    user_input = input("Придумайте пароль: ")
    len_password = len(user_input)

    for sym in user_input:
        if sym.isupper():
            upper_sym = True
        elif sym.isdigit():
            count_digit += 1

    if upper_sym == False or count_digit < 3 or len_password <8:
        print("Пароль ненадёжный. Попробуйте ещё раз!!!")
    else:
        print("Это надежный пароль")
