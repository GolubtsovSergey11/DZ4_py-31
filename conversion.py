#Напишите код для преобразования произвольного списка вида
# ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины)
# в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}


my_list = ['2018-01-01', 'yandex', 'cpc', 100]

result = my_list.pop()

for item in reversed(my_list):
    result = {item: result}

print(result)
