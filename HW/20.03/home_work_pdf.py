# 5.Домашнее PDF задание 19
# Задача 1)

def calculate_min_payment(prices):
    prices.sort(reverse=True)
    two_most_expensive = prices[:2]
    remaining_prices = prices[2:]
    total_payment = sum(remaining_prices)
    return total_payment

# Ввод стоимостей товаров
# N = int(input("Введите количество товаров: "))
# prices = []
# for i in range(N):
#     price = int(input("Введите стоимость товара: "))
#     prices.append(price)
#
#
# min_payment = calculate_min_payment(prices)
#
# print("Минимальная сумма денег:", min_payment)
#

# Задача 2)




# def find_closest_pair(numbers):
#     sorted_numbers = sorted(numbers)
#     min_diff = float('inf')
#     closest_pair = None
#
#     for i in range(len(sorted_numbers) - 1):
#         diff = sorted_numbers[i + 1] - sorted_numbers[i]
#
#         if diff < min_diff:
#             min_diff = diff
#             closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
#
#     return closest_pair
#
#
# numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
#
#
# closest_pair = find_closest_pair(numbers)
#
#
# print(*closest_pair)





# 5.Домашнее PDF задание 20




# def align_strings(strings):
#     max_length = max(len(string) for string in strings)
#
#     aligned_strings = []
#     for string in strings:
#         stars = "*" * (max_length - len(string))
#         aligned_string = stars + string
#         aligned_strings.append(aligned_string)
#
#     return aligned_strings
#

# M = int(input("Введите количество строк: "))
# strings = []
# for i in range(M):
#     string = input("Введите строку: ")
#     strings.append(string)
#

# aligned_strings = align_strings(strings)
#

# for aligned_string in aligned_strings:
#     print(aligned_string)


# 2)

def add_element_to_array(array):
    positive_sum = sum([num for num in array if num > 0])
    negative_sum = sum([num for num in array if num < 0])

    negative_sum_abs = abs(negative_sum)

    difference = negative_sum_abs - positive_sum

    array.append(difference)

    return array


N = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(N):
    element = int(input("Введите элемент массива: "))
    array.append(element)


new_array = add_element_to_array(array)


print(new_array)
print("Добавленный элемент:", new_array[-1])
