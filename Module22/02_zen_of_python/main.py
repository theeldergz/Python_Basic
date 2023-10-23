text_zen = open('zen.txt', 'r')
text_by_line = text_zen.readlines()
text_zen.close()

for line in text_by_line[::-1]:
    print(line, end='')
