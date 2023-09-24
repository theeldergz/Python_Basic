violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

user_list = []
total_duration = 0
count_music = int(input("Сколько песен выбрать? "))

for i in range(1, count_music + 1):
    user_choice = input(f"Название {i}-й песни: ")
    for song_index, song in enumerate(violator_songs):
        if user_choice == violator_songs[song_index][0]:
            total_duration += violator_songs[song_index][1]
            user_list.append(user_choice)

print("Список ваших треков: ", user_list, "Общее время звучания: ", round(total_duration, 2), "минуты")
