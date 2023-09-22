check_palindrome = list(input("Введите слово для проверки: "))
check_palindrome_2 = []
check_palindrome_2.append(check_palindrome[::-1])

if check_palindrome == check_palindrome_2[0]:
    print("Да это палиндром")
else:
    print("Нет это не палиндром")

# print(check_palindrome)
# count = 0
#
# for index, sym in enumerate(check_palindrome):
#     if check_palindrome[index] == check_palindrome[-index - 1]:
#         count += 1
#     if count == len(check_palindrome):
#         print("Да это палиндром")
#     else:
#         print("Нет этон е палиндром")