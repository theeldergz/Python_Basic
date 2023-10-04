user_input = input("Введите ip: ")
permitted_sym = [str(sym) for sym in range(10)]
permitted_sym.append(".")
len_flag = False
num_flag = True
max_num_flag = True

for sym in user_input:
    if sym not in permitted_sym:
        num_flag = False
        break

if num_flag:
    check_ip = user_input.split(".")
    check_ip_integer = [int(num) for num in check_ip]
    for index, value in enumerate(check_ip_integer):
        if index == 3:
            len_flag = True

        if value < 0:
            print("\n", value, "Меньше чем 0")
            max_num_flag = False
            break
        elif value > 255:
            print("\n", value, "Больше чем 255")
            max_num_flag = False
            break

if len_flag == False or num_flag == False:
    print("\nНеверный ввод. IP — это четыре числа, разделённые точками.")

if len_flag and max_num_flag and num_flag:
    print("\nДа адрес подходит")
    print(f'Флаг длины {len_flag}, флаг диапазона цифр {max_num_flag}, флаг совпадения кол-ва триплетов {num_flag}')
