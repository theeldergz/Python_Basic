check_palindrome = input("Введите слово для проверки: ")

if check_palindrome == check_palindrome[::-1]:
    print("Да это палиндром!")
else:
    print("Нет это не палиндром!")
