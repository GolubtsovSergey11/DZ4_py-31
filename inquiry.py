#Задание 3. Дан список поисковых запросов. Получить распределение количества слов в них.
# Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'Смотреть онлайн Лига Чемпионов'
]

new_list = []
new_dict = {}

for word in queries:
    res = len(word.split())
    new_list.append(res)
    new_dict[res] = new_list.count(res)

for key, value in new_dict.items():
    result = value / len(queries) * 100
    print(f'Поисковых запросов по {key} словам: {round(result)} %')
