analysys_dict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

text = open('text.txt', 'r')

for line in text:
    line = line.lower()
    for sym in line:
        if sym in alphabet:
            analysys_dict[sym] = analysys_dict.get(sym, 0) + 1

text.close()



summ_symbols = sum(analysys_dict.values())
sorted_keys = [key for key in analysys_dict.keys()]
sorted_keys.sort()
frequency = [analysys_dict[key] for key in sorted_keys]

for index1, num1 in enumerate(frequency):
    for index2, num2 in enumerate(frequency):
        if frequency[index1] > frequency[index2]:
            frequency[index1], frequency[index2] = frequency[index2], frequency[index1]
            sorted_keys[index1], sorted_keys[index2] = sorted_keys[index2], sorted_keys[index1]


analysys = open('analysis.txt', 'w')

for key in sorted_keys:
    frequency_result = str(round(analysys_dict[key] / summ_symbols, 3))
    line_analysys = key + '\t' + frequency_result + '\n'
    analysys.write(line_analysys)

analysys.close()
