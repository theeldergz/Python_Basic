class Stack:
    def __init__(self):
        self.__task_list = list()

    def add_in_stack(self, task):
        self.__task_list.append(task)

    def del_from_stack(self):
        if len(self.__task_list) == 0:
            return None
        return self.__task_list.pop()

    def __str__(self):
        return str(self.__task_list)


class TaskManager:
    def __init__(self):
        self.__task_dict = dict()

    def __is_double(self, task):
        for key in self.__task_dict.keys():
            temp_list = list()
            del_elem = ''
            while del_elem is not None:
                del_elem = self.__task_dict[key].del_from_stack()
                if del_elem is not task:
                    temp_list.append(del_elem)
                else:
                    temp_list.append(del_elem)
                    return True
            else:
                temp_list.pop()
                temp_list.reverse()
                for index, _ in enumerate(temp_list):
                    self.__task_dict[key].add_in_stack(temp_list[index])


    def new_task(self, task, priority):
        if self.__is_double(task):
            print('Такая задача уже есть!')

        if priority not in self.__task_dict:
            self.__task_dict[priority] = Stack()
        self.__task_dict[priority].add_in_stack(task)

    def del_task(self, task):
        for key in self.__task_dict.keys():
            temp_list = list()
            del_elem = ''
            while del_elem is not None:
                del_elem = self.__task_dict[key].del_from_stack()
                if del_elem is not task:
                    temp_list.append(del_elem)
                else:
                    pass
            else:
                temp_list.pop()
                temp_list.reverse()
                for index, _ in enumerate(temp_list):
                    self.__task_dict[key].add_in_stack(temp_list[index])




    def __str__(self):
        return_line = list()
        for key in sorted(self.__task_dict.keys()):
            return_line.append(f'{key}: {self.__task_dict[key]}\n')

        return ''.join(return_line)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.del_task('помыть посуду')
print(manager)
manager.new_task("поесть", 2)