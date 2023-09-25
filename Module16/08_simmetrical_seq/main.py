N = int(input("Введите кол-во чисел в последовательности: "))
nums = []
nums_right = []
not_equal_count = 0

for i in range(1, N + 1):
    nums.append(int(input(f"Введите число {i}: ")))

if nums[::] == nums[::-1]:
    print("Последовательность уже симметрична!")
else:
     for index in range(N):
        mid = nums[N-1::]
        left = nums[N - (1 + index):N - (index):]
        if mid != left:
            nums.extend(left)
            nums_right.extend(left)
            not_equal_count += 1


print("Новая последовательноть: ",*nums)
print("Минимальное кол-во чисел которые нужно приписать: ", not_equal_count)
print("Числа которые необходимо приписать", *nums_right)

