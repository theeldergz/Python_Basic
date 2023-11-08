import random

NAMES = [
            'Мария', 'Екатерина', 'Елена', 'Анна',
            'Анастасия', 'Альбина', 'Ольга', 'Елена',
            'Александр', 'Иван', 'Андрей', 'Алексей',
            'Дмитрий', 'Максим'
         ]

SURNAMES = [
            'Иванов(а)', 'Смирнов(а)', 'Петров(а)',
            'Васильев(а)', 'Кузнецов(а)', 'Романов(а)',
            'Сафин(а)', 'Шакиров(а)', 'Хайруллин(а)',
            'Зарипов(а)', 'Закиров(а)'
            ]

GROUPS = ['1A', '2B', '3C', '4D']


class Student:

    def __init__(self, name, group, *args):
        self.name = name
        self.group = group
        self.performance = args[0]

    def middle_marks(self):
        summ = 0

        for mark in self.performance:
            summ += mark
        return summ / 5

    def info(self):
        print(f'Привет я {self.name}, из группы {self.group},'
              f' мои оценки {self.performance},'
              f' мой средний балл {self.middle_marks()}\n')


student_list = []

for _ in range(10):

    name = random.choice(NAMES) + " " + random.choice(SURNAMES)
    marks = [random.randint(1, 5) for _ in range(5)]
    group = random.choice(GROUPS)
    student = Student(name, group, marks)
    student.info()

    student_list.append([name, group, student.middle_marks()])

for index1 in range(len(student_list)):
    for index2 in range(len(student_list)):
        if student_list[index1][2] < student_list[index2][2]:
            student_list[index1][2], student_list[index2][2] = student_list[index2][2], student_list[index1][2]

for student in student_list:
    student_name, student_group, student_mark = student
    print(f'Студент {student_name} из группы {student_group} набрал средний балл: {student_mark}')

# student_list = {}
#
# for _ in range(10):
#
#     name = random.choice(NAMES) + " " + random.choice(SURNAMES)
#     marks = [random.randint(1, 5) for _ in range(5)]
#     group = random.choice(GROUPS)
#     student = Student(name, group, marks)
#     student.info()
#
#     if student.middle_marks() not in student_list:
#         student_list[student.middle_marks()] = name
#     else:
#         temp_list = []
#         temp_name = student_list.pop(student.middle_marks())
#         temp_list.append(temp_name)
#         temp_list.append(name)
#         student_list[student.middle_marks()] = temp_list
#
# sorted_students_list = sorted(student_list.keys())
#
#
#
# def print_sort_student(sortetd_list):
#     for key in sortetd_list:
#         print(f'\tУ студента(ов): {student_list[key]}, средний балл: {key} ')
