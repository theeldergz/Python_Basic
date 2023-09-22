N = int(input("Введите кол-во элементов табло: "))
K = int(input("Введите значение сдвига: "))
nums = []
K_1 = N - K

for i in range(1, N+ 1):
    num = int(input(f"Введите {i} цифру которая должна быть на табло: "))
    nums.append(num)

print(*nums[K_1:N] + nums[:K_1])
