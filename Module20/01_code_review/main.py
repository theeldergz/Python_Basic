students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def stud_interest(user_dict):
    list_intersts = []
    max_len_surname = 0
    for student_id in user_dict:
        list_intersts.append(user_dict[student_id]['interests'])
        max_len_surname += len(user_dict[student_id]['surname'])
    return list_intersts, max_len_surname


interests, len_surname = stud_interest(students)
id_age_list = [(id, students[id]['age']) for id in students]

print('\nCписок пар "ID студента — возраст":', id_age_list,
      "\nПолный список интересов всех студентов: ", *interests,
      "\nОбщая длина всех фамилий студентов: ", len_surname)




