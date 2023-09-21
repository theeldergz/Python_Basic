all_containers = []
new_all_containers = []
count = 0
final_count = 0

containers_count = int(input("Количество контейнеров: "))

for container in range(1, containers_count + 1):
    mass = int(input(f"Введите вес {container} контейнера: "))
    all_containers.append(mass)
all_containers.sort(reverse=True)

new_container = int(input("\nВведите вес нового контейнера: \n"))

for mass_container in all_containers:
    if new_container >= mass_container:
        if new_container not in new_all_containers:
            new_all_containers.append(new_container)
            final_count = count
        elif new_container in new_all_containers:
            new_all_containers.append(mass_container)
            final_count = count
            continue
    count += 1
    new_all_containers.append(mass_container)

print(f"Номер, который получит новый контейнер: {final_count + 1}", "\nРасположение контейнеров:", new_all_containers)