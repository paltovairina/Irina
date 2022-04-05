# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


import random

my_array = [random.randint(-100, 100) for _ in range(20)]
random.shuffle(my_array)
print(my_array)


def bubble_sort(array):
    end = True
    n = 0
    while (end):
        end = False
        for i in range(len(array) - n - 1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                end = True
        n += 1
    return array, n


print(bubble_sort(my_array))
# благодаря оптимизации мы уменьшили количество циклов сортировки с 20 до 16
