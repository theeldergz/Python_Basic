text = input("Введите строку:\t")


def start(text):
    last_h = 0
    first_h = text.index("h")
    for count, value in enumerate(text):
        if value == "h":
            last_h = count
    return first_h, last_h


start, stop = start(text)
print("Развёрнутая последовательность между первым и последним h: ", text[stop -1:start:-1])