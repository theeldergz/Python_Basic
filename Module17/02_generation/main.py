N = int(input("Введите число: "))

nums = [num % 5 if num % 2 != 0 else 1 for num in range(N)]

print(nums)
