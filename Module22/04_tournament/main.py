first_tour = open('first_tour.txt')
first_tour_by_lines = first_tour.readlines()
first_tour.close()

count_winners = 0
winners_list = {}
need_point = first_tour_by_lines[0]

second_tour = open('second_tour.txt', 'w')

for line in first_tour_by_lines[1:]:
    player_info = line.split()
    if player_info[2] > need_point:
        count_winners += 1
        player_info[1] = player_info[1][:1] + "."
        winners_list[player_info[2]] = player_info[1], player_info[0], player_info[2], '\n'


winners_list_keys = [int(key) for key in winners_list.keys()]
winners_list_keys.sort(reverse=True)

second_tour.write(str(count_winners) + '\n')

for key in winners_list_keys:
    second_tour.write(' '.join(winners_list[str(key)]))

second_tour.close()


