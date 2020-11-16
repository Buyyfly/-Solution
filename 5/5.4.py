# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

ac = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

with open('4.txt', 'r', encoding='UTF=8') as f:
    with open('4_end.txt', 'w', encoding='UTF=8') as new_f:
        for el in f:
            spl = el.split()
            spl[0] = ac.get(int(spl[2]))
            new_f.write(f'{" ".join(spl)}\n')