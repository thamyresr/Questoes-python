import numpy as np


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read().split()
        return data
    except FileNotFoundError as error:
        print(str(error))
        return []


def convert_number(original_list):
    new_list = []
    for value in original_list:
        try:
            new_list.append(int(value))
        except ValueError:
            print(value, 'The value is not a valid number.')
            new_list.append(0)
    return new_list


list_a = read_file('a.txt')
list_b = read_file('b.txt')

list_a = convert_number(list_a)
list_b = convert_number(list_b)

print('List A:', list_a)
print('List B:', list_b)

size_a = len(list_a)
size_b = len(list_b)

if size_a < size_b:
    list_a[size_a:size_b] = (size_b - size_a) * [0]
else:
    list_b[size_b:size_a] = (size_a - size_b) * [0]

print('Result:', np.array(list_a) + np.array(list_b))
