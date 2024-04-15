import numpy as np
from main import generate_sbox, sbox_forward, sbox_backward, pbox_permutation

# Генеруємо випадкові дані для тестування
input_data = np.random.randint(0, 256, size=(8, 8), dtype=np.uint8)

# Генеруємо випадкову таблицю констант S-блоку
sbox = generate_sbox()

# Пряме перетворення за алгоритмом S-блоку
encrypted_data = sbox_forward(input_data, sbox)

# Зворотне перетворення за алгоритмом S-блоку
decrypted_data = sbox_backward(encrypted_data, sbox)

# Перестановка P-блоку
permuted_data = pbox_permutation(input_data)

print("Вхідні дані:")
print(input_data)
print("Зашифровані дані:")
print(encrypted_data)
print("Розшифровані дані:")
print(decrypted_data)
print("Переставлені дані:")
print(permuted_data)
