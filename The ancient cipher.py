import random
multiple = []
second_field = []
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
first_field = random.choice(range(3, 20))
for i in list_:
    if i != 1:
        if first_field % i == 0:
            multiple.append(i)
        else:
            continue
#print('Число первого поля:',first_field, '  ', 'Кратные числа второго поля:',*multiple)
for j in range(len(list_)):
    for s in range(j + 1, len(list_)):
        for m in range(len(multiple)):
            if list_[j] + list_[s] == multiple[m]:
                second_field.append(list_[j])
                second_field.append(list_[s])
            else:
                continue
print('Число первого поля:',first_field, '  ','Числа второго поля:', *second_field)



