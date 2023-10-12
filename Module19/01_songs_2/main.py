violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

max_duration = 0
user_song_count = int(input("Сколько песен выбрать?:  "))
for song in range(user_song_count):
    song_add = input("Введите {} песню: ".format(song + 1))
    max_duration += violator_songs[song_add]

print("Общее время звучания песен: ", round(max_duration, 2), "минуты")
