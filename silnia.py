# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)

# print(fact(4))

# def sum(arr):
#     if arr == []:
#         return 0
#     else:
#         return arr[0] + sum(arr[1:])

# print(sum([2,4,6]))

def count(lst):
        if lst == []:
            return 0
        else:
            return 1 + count(lst[1:])

print(count([1,3,4,9,111]))