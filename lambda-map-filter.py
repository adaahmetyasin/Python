square = lambda n: n ** 2
liste = [1, 2, 3, 4,5]

result = list(map(square,liste))
result2 = list(map(lambda n: n * 2,[5, 7, 9]))
print(result)
print(result2)

def double(x):
    return x*2
result3 = list(map(double, liste))
print(result3)

strs = ['apple', 'and', 'a', 'donut']
result4 = list(filter(lambda s: len(s) > 3, strs))
print(result4)

result5 = list(filter(lambda n: n % 2 == 0, liste))
print(result5)