from itertools import islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Михаил'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

# Не знаю почему, но мне показалось, что из списка классов нужно убрать повторы


def unique(seq):
    klass_tmp_list = set()
    klass_tmp_list_add = klass_tmp_list.add
    return [x for x in seq if not (x in klass_tmp_list or klass_tmp_list_add(x))]


output_klass = unique(klasses)


def tutor_klass():
    for num in range(len(tutors)):
        if num < len(output_klass):
            tutor_list = (tutors[num], output_klass[num])
        else:
            tutor_list = (tutors[num], 'None')
        yield tutor_list


print_gen = tutor_klass()
print(type(print_gen))
print(*islice(print_gen, len(tutors)))
print(next(print_gen))

