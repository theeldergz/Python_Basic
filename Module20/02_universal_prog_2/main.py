def is_prime(iterator):
    lenght_crypto = len(iterator)
    prime_list = []
    for number in range(lenght_crypto):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime_list.append(number)

    crypto_list = [value for index, value in enumerate(iterator) if index in prime_list]

    return crypto_list


def crypto(iterator):
    return is_prime(iterator)


