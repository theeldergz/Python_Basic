
def count_sum(nums):
    summ = 0
    while nums > 0:
        summ += nums % 10
        nums //= 10
    print(f"\nСумма чисел: {summ}")
    return(summ)

def count_sym(nums):
    count = 0
    while nums > 0:
        count += 1
        nums //= 10
    print(f"\nКоличество цифр в числе: {count}")
    return(count)

x_num = int(input("\nВведите число: "))

summ_number = count_sum(x_num)
count_number = count_sym(x_num)

print("\nРазность суммы и количества цифр: ", summ_number - count_number)