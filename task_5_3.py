# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Михаил'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def unique(seq):
    klass_tmp_list = set()
    klass_tmp_list_add = klass_tmp_list.add
    return [x for x in seq if not (x in klass_tmp_list or klass_tmp_list_add(x))]


output_klass = unique(klasses)
print(output_klass)
#
# tutors_list = frozenset(tutors)
# print(tutors_list)
# klasses_list = frozenset(klasses)
# print(klasses_list)
# tuple_gen = tutors_list.intersection(klasses_list)
# print(tuple_gen)
# комментарий - не лучшее решение, так как в функцию явно не передаются списки в виде параметров.
# Лучше передавать исходные данные в явном виде + плохо, что присоединяется : отдельно, выполнить
# форматирование отдельно при выводе. Возможно рассмотреть вариант из третьего урока, setdefault 'None'
#

# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
#
#
# Эта запись называется Generator Expression (генераторное выражение). В первой позиции мы описываем
# очередное возвращаемое генератором значение — в нашем случае квадрат числа. Дальше пишем цикл, в котором
# создаются исходные данные для этих значений. У нас это нечётные числа до миллиона включительно.
# А если нужен генератор английских букв? Попробуем:

# eng_letters_gen = (chr(code) for code in range(ord('a'), ord('z') + 1))
# print(*eng_letters_gen, sep='')  # abcdefghijklmnopqrstuvwxyz

#
# length_tutor = len(tutors)
# length_klasses = len(klasses)
#
# for el in (output_klass) for tutors in range(1, len(tutors))):
#     yield tutors,el
    #yield (tutors[i] + ":" , output_klass[i])
    # else:
    #     yield (tutors[i] + ':', 'None')

#tutor_klasses = (klass(output_klass) for tutor in range[tutors])


def tutor_klass(tut, klass):
    for el in range(0, len(tut)):
        for i in range(0, len(klass)):
            #tutor_list_add = tutor_list.add
        #tutor_list.add(tutors[el])
        #tutor_list.add(output_klass[el])
        #yield tutors[el]#, output_klass[el]
        #for i in range(0, len(output_klass)):
        #yield el, i
        #yield tutor_list
            #tutor_list = (tut[el], klass[i])
            yield tut[el], klass[i]
            #return tutor_list


#output = tutor_klass(tutors, output_klass)
#print(type(output))
#print(output)
#print(tutor_klass(tutors, output_klass))
#print(*output)
# output = (klass(output_klass) for tutor in range(int(tutors)))
# print(type(output))
print(next(tutor_klass(tutors, output_klass)))
print(next(tutor_klass(tutors, output_klass)))
print(next(tutor_klass(tutors, output_klass)))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
