def foo(num):
    if num == 0:
        return 0
    foo(num - 1)
    print(num)


test_num = int(input("Введите num: "))
foo(test_num)

