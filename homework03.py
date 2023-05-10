import random

numbers = list(random.randint(1,10) for _ in range(10))
unique_numbers = set(numbers)
deleted_numbers = int((len(numbers))-len(unique_numbers))
print(f'{numbers} => {deleted_numbers} элеманта совподают \n Список уникальных элемантов {unique_numbers}')