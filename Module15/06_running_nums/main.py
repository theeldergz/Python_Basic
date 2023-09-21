N = int(input("Введите кол-во элементов табло: "))
K = int(input("Введите значение сдвига: "))
nums = []
count = N

for i in range(1, N+ 1):
    num = int(input(f"Введите {i} цифру которая должна быть на табло: "))
    nums.append(num)

for index, number in enumerate(nums):
    print(nums[index])

