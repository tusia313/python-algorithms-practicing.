# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)

# print(fact(4))

def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])

print(sum([2,4,6]))