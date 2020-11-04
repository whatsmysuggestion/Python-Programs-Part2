def sq(n):
    return n * n


numbers = (11, 21, 32, 43)
result = map(sq, numbers)
print(list(result))