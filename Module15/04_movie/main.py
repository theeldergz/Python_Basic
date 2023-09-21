films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

start_films_pak = []

count_films = int(input("Сколько фильмов вы хотите добавить?:  "))

for i in range(1, count_films + 1):
    user_films_choice = input(f"Введите название {i} фильма: ")
    if user_films_choice in films:
        start_films_pak.append(user_films_choice)
    else:
        print("\nТакого фильма у нас нет!")

print("\nВаш список любимых фильмов: ",end="")

for film in start_films_pak:
    print(film, end=", ")