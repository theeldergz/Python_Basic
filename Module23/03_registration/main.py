def bad_logs(info_list, exc):
    with open('registrations_bad.log', 'a', encoding='utf-8') as registrations_bad:
        registrations_bad.write(' '.join(info_list))
        registrations_bad.write('\t----->\t')
        registrations_bad.write(exc)
        registrations_bad.write('\n')


def good_logs(info_list):
    with open('registrations_good.log', 'a', encoding='utf-8') as registrations_good:
        registrations_good.write(' '.join(info_list))
        registrations_good.write('\n')


def bad_logins(info_list):
    try:
        if not info_list:
            info_list_none = ['None', 'None', 'None']
            bad_logs(info_list_none, 'НЕ присутствуют все три поля')
            raise IndexError

        if not info_list[0].isalpha():
            bad_logs(info_list, 'Поле «Имя» содержит НЕ только буквы')
            raise NameError

        if info_list[1].endswith('.com') or info_list[1].endswith('.ru'):
            if '@' not in info_list[1]:
                bad_logs(info_list, 'Поле «Имейл» НЕ содержит @ и . (точку)')
                raise SyntaxError

        if not info_list[2].isdigit():
            bad_logs(info_list, 'Поле «Возраст» НЕ является числом от 10 до 99')
            raise ValueError

    except (IndexError, NameError, SyntaxError, ValueError):
        pass

    else:
        good_logs(info_list)


with open('registrations.txt', encoding='utf-8') as registrations:
    for line in registrations:
        user_info = line.split()
        bad_logins(user_info)
