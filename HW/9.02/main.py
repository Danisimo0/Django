# 2

# def is_balanced(expression):
#     stack = []
#     opening_brackets = ['(', '{', '[']
#     closing_brackets = [')', '}', ']']
    
#     for char in expression:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if len(stack) == 0:
#                 return False
#             last_opening = stack.pop()
#             if opening_brackets.index(last_opening) != closing_brackets.index(char):
#                 return False
    
#     return len(stack) == 0
 
# expression = "({})"
# if is_balanced(expression):
#     print(f"Выражение '{expression}' сбалансировано")
# else:
#     print(f"Выражение '{expression}' несбалансировано")

# 3


def find_intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    intersection = set1.intersection(set2)
    
    return list(intersection)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3]
intersection = find_intersection(nums1, nums2)
print("Пересечение массивов:", intersection)
