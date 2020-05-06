#Напишите код для преобразования произвольного списка вида
# ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины)
# в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}


my_list = ['2018-01-01', 'yandex', 'cpc', 100]

result = my_list[-1]

for item in my_list[::-1]:
    result = {item: result}

print(result)
