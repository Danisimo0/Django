# file 1
# 1)
# def is_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
#
# input_numbers = input("Введите три целых числа a, b, c, разделенных пробелами: ")
# numbers = input_numbers.split()
#
# for i in range(0, len(numbers), 3):
#     a, b, c = map(int, numbers[i:i+3])
#     if is_triangle(a, b, c):
#         print("true", end=" ")
#     else:
#         print("false", end=" ")
#


# 2

# def is_even(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
#
# input_a = input("Введите целое число a: ")
#
# a = int(input_a)
#
# if is_even(a):
#     print("True")
# else:
#     print("False")


# 3

def is_sum_greater(a, b, c):
    if a + b > c:
        return True
    else:
        return False


input_a = input("Введите первое целое число a: ")
input_b = input("Введите второе целое число b: ")
input_c = input("Введите третье целое число c: ")

a = int(input_a)
b = int(input_b)
c = int(input_c)

if is_sum_greater(a, b, c):
    print("true")
else:
    print("false")


# 4
def is_first_greater(a, b):
    if a > b:
        return True
    else:
        return False


input_a = input("Введите первое целое число a: ")
input_b = input("Введите второе целое число b: ")

a = int(input_a)
b = int(input_b)

if is_first_greater(a, b):
    print("true")
else:
    print("false")
