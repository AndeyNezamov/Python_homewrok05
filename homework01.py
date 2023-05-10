import random
numbers = [random.randint(1,10) for _ in range(int(input('Введите длинну списка: ')))]
print(numbers)
numbers = list(filter(lambda x: x>5, numbers))
print(numbers)