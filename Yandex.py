#Дана статистика рекламных каналов по объемам продаж. Напишите скрипт,
# который возвращает название канала с максимальным объемом.
# Т. е. в данном примере скрипт должен возвращать 'yandex'.

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

if max(stats.values()) in stats.values():
    print(max(stats.items()))

