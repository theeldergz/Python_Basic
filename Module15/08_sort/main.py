import random
N = int(input("Введите кол-во элементов: "))
nums = []

for index_num in range(N):
    # nums.append(int(input(f"Введите {index_num + 1} элемент: ")))
    nums.append(random.randint(1, 99))
print("Начальный список элементов: ", *nums)

for index_i, num_i in enumerate(nums):
    for index_j, num_j in enumerate(nums):
        if nums[index_i] < nums[index_j]:
            nums[index_i], nums[index_j] = nums[index_j], nums[index_i]

print("Упорядоченный список элементов: ", *nums)