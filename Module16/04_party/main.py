guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    max_guests = len(guests)
    print(f"Сейчас на вечеринке {max_guests} человек: ", *guests, "\n")
    user_answer = input("Гость пришёл или ушёл?: ")

    if user_answer.lower() == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break


    guest_name = input("Имя гостя: ")

    if user_answer.lower() == "пришел":
        if max_guests + 1 == 7:
            print(f"Прости, {guest_name.capitalize()},но мест нет( ")
        else:
            guests.append(guest_name.capitalize())
            print(f"Привет, {guest_name.capitalize()}!")

    elif user_answer.lower() == "ушел":
        if guest_name in guests:
            guests.remove(guest_name.capitalize())
            print(f"Пока, {guest_name.capitalize()}")
        else:
            print("Такого гостя нет в списке")