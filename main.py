# Таблиця замін для S-блоку
S_BOX = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

# Функція для S-блоку
def s_box(input):
    input1 = input[:4] # Перші 4 біти
    input2 = input[4:] # Останні 4 біти

    row1 = int(input1[0] + input1[3], 2) # Визначення рядка для першої тетради
    col1 = int(input1[1:3], 2) # Визначення стовпця для першої тетради
    row2 = int(input2[0] + input2[3], 2) # Визначення рядка для другої тетради
    col2 = int(input2[1:3], 2) # Визначення стовпця для другої тетради

    output1 = format(S_BOX[row1][col1], '04b') # Вихідна перша тетрада
    output2 = format(S_BOX[row2][col2], '04b') # Вихідна друга тетрада

    return output1 + output2 # Повертаємо об'єднані результати обробки обох тетрад

# Функція для зворотного S-блоку
def reverse_s_box(input):
    output = ""
    for char in input:
        index = S_BOX[int(char, 2)].index(int(char, 2))
        output += format(index, '04b')
    return output

# Функція для P-блоку (перестановка)
def p_box(input):
    output = ""
    for index in [2, 4, 6, 8, 1, 3, 5, 7]:
        output += input[index - 1]
    return output

# Функція для зворотного P-блоку (перестановка)
def reverse_p_box(input):
    output = ""
    for index in [5, 1, 3, 7, 2, 4, 6, 8]:
        output += input[index - 1]
    return output

# Перевірка роботи функцій
def test():
    input_data = "10101010"
    s_result = s_box(input_data)
    print("S-блок прямого перетворення:", s_result)
    reverse_s_result = reverse_s_box(s_result)
    print("S-блок зворотного перетворення:", reverse_s_result)

    p_result = p_box(input_data)
    print("P-блок прямого перетворення:", p_result)
    reverse_p_result = reverse_p_box(p_result)
    print("P-блок зворотного перетворення:", reverse_p_result)

test()
