text1 = input("Введите 1ую строку: ")
text2 = input("Введите 2ую строку: ")
answer = ""
lenght_txt2 = len(text2)
equal_string_flag = False

for index, value in enumerate(text2, start=1):
    answer = text2[lenght_txt2 - index:] + text2[:lenght_txt2 - index]
    if answer == text1:
        equal_string_flag = True
        count = index
    answer = ""

if equal_string_flag:
    print("Первая строка получается из второй со сдвигом ", count)
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")


