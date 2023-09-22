gpu = [3070, 2060, 3090, 3070, 3090]
gpu_in_stock = []
high_model = 0

for model in gpu:
    if model >= high_model:
        high_model = model

for model in gpu:
    if model != high_model:
        gpu_in_stock.append(model)

print(gpu_in_stock)


