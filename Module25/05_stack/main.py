import copy


class Steck:
    def __init__(self):
        self.__temp_list = list()
        self.__value_list = list()
        self.__temp_del_list = list()

    def add_value(self, __value):
        if __value in self.__value_list:
            raise ValueError('уже есть в списке')
        self.__value_list.insert(0, __value)

    def del_value(self, __value):
        while True:

            if len(self.__value_list) == 0:
                break

            if self.__value_list[0] == __value:

                search_elem = self.__value_list.pop(0)
                self.__temp_del_list.append(search_elem)

            else:

                temp_elem = self.__value_list.pop(0)
                self.__temp_list.append(temp_elem)

        self.__temp_list.reverse()
        for elem in self.__temp_list:
            self.__value_list.insert(0, elem)

        return self.__temp_del_list[0]


class TaskManager(Steck):
    def __init__(self):
        super().__init__()
        self.__task_dict = dict()

    def __str__(self):
        task_dict_keys = self.__task_dict.keys()
        task_dict_keys = sorted(task_dict_keys)
        info_string = '\nСписок задач:'
        for key in task_dict_keys:
            if isinstance(self.__task_dict[key], list):
                list_string = '; '.join(self.__task_dict[key])
                info_string += f'\n{key}: ' + list_string
            else:
                info_string += f'\n{key}: {self.__task_dict[key]}'

        return info_string

    def new_task(self, __task: str, __priority: int):
        if __priority in self.__task_dict:
            __old_task = self.__task_dict.pop(__priority)
            self.__task_dict.setdefault(__priority, [__old_task, __task])
        else:
            self.__task_dict.update({__priority: __task})

        self.add_value(__task)

    def del_task(self, __value):
        self.del_value(__value)
        __temp_dict_copy = copy.deepcopy(self.__task_dict)

        for key, task in __temp_dict_copy.items():
            if isinstance(task, list):
                for elem in task:
                    if elem == __value:
                        task.remove(elem)
                        self.__task_dict[key] = task

            else:
                if task == __value:
                    self.__task_dict.pop(key)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

manager.del_task('помыть посуду')
print(manager)
