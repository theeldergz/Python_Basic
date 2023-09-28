nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

answer = [nice_list[index1][index2][index3]
          for index1 in range(len(nice_list))
          for index2 in range(len(nice_list[index1]))
          for index3 in range(len(nice_list[index2 - 1]))]

print(answer)
