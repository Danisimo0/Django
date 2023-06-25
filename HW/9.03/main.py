# 1 )
# from myapp.models import MyModel
#
# # Циклом изменяем все заголовки моделей
# for model in MyModel.objects.all():
#     model.title = f"{model.title} ({model.id})"
#     model.save()
#
# # Удаляем записи с нечетными цифрами в заголовке
# for model in MyModel.objects.all():
#     if any(char.isdigit() and int(char) % 2 != 0 for char in model.title):
#         model.delete()


# File 2)

# 1)
# def find_missing_card(N, cards):
#     total_sum = N * (N + 1) // 2
#     sum_of_cards = sum(cards)
#     missing_card = total_sum - sum_of_cards
#     return missing_card
#
# N = int(input("Введите число N: "))
# cards = []
# for _ in range(N - 1):
#     card = int(input("Введите номер оставшейся карточки: "))
#     cards.append(card)
#
# missing_card = find_missing_card(N, cards)
# print("Потерянная карточка:", missing_card)


# 2)
def print_squares(N):
    i = 1
    while i ** 2 <= N:
        print(i ** 2, end=" ")
        i += 1


N = int(input("Введите число N: "))
print("Квадраты натуральных чисел, не превосходящие N:")
print_squares(N)
