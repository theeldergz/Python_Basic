text = input("Введите строку: ")
new_text = []
equal_count = 1

for sym in range(1, len(text)):
    if text[sym - 1] == text[sym]:
        equal_count +=1
    else:
        new_text.append(text[sym - 1])
        new_text.append(equal_count)
        equal_count = 1

if len(text):
    new_text.append(text[-1])
    new_text.append(equal_count)

answer = [str(sym) for sym in new_text]

print("".join(answer))
