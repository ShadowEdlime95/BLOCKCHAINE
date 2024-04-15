import numpy as np

# Функції S-блоку та P-блоку

def generate_sbox():
    
    #Функція для генерації випадкової таблиці констант S-блоку.
    
      sbox = np.random.randint(0, 256, size=(16, 16), dtype=np.uint8)
    return sbox

def sbox_forward(input_data, sbox):
    
    #Функція для прямого перетворення за алгоритмом S-блоку.
    
    output_data = np.zeros_like(input_data, dtype=np.uint8)
    for i in range(input_data.shape[0]):
        for j in range(input_data.shape[1]):
            row = (input_data[i, j] >> 4) & 0x0F
            col = input_data[i, j] & 0x0F
            output_data[i, j] = sbox[row, col]
    return output_data

def sbox_backward(output_data, sbox):
    
    #Функція для зворотного перетворення за алгоритмом S-блоку.
    
    input_data = np.zeros_like(output_data, dtype=np.uint8)
    for i in range(output_data.shape[0]):
        for j in range(output_data.shape[1]):
            for row in range(16):
                for col in range(16):
                    if sbox[row, col] == output_data[i, j]:
                        input_data[i, j] = (row << 4) | col
                        break
    return input_data

def pbox_permutation(input_data):
    
    #Функція для перестановки P-блоку, яку я вибрав.
    
    pbox_permutation = [16, 7, 20, 21, 29, 12, 28, 17,
                        1, 15, 23, 26, 5, 18, 31, 10,
                        2, 8, 24, 14, 32, 27, 3, 9,
                        19, 13, 30, 6, 22, 11, 4, 25]
    output_data = np.zeros_like(input_data)
    for i, idx in enumerate(pbox_permutation):
        output_data[i // 8, i % 8] = input_data[(idx - 1) // 8, (idx - 1) % 8]
    return output_data

if __name__ == "__main__":
    # Для тих, хто хоче перевірити в цьому файлі дійсність коду я залишаю це поле.
    pass
