"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import csv
from decimal import Decimal


def select_animals(input_path, output_path, compressed=False):
    ret = []
    header = None
    with open(input_path, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=',')
        header = next(reader, None)
        dict_reader = csv.DictReader(input_file, delimiter=',', fieldnames=header)
        prefix = {'kg': 1, 'g': 1e-3, 'mg': 1e-6, 'Mg': 1e3}
        genera = set()  # genera stands for plural of genus

        for row in dict_reader:
            genera.add(row['genus'])

        for genus in genera:
            for gender in ['male', 'female']:
                input_file.seek(0)
                probes = []
                masses = []
                for row in dict_reader:
                    if row['gender'] == gender and row['genus'] == genus:
                        probes.append(row)
                        mass = row['mass'].split(' ')
                        fixed_mass = float(mass[0]) * prefix[mass[1]]   # fixing prefixes likes kg, mg etc.
                        masses.append(fixed_mass)
                ret.append([x for _, x in sorted(zip(masses, probes))][0])

        ret = sorted(ret, key=lambda i: (i['genus'], i['name']))

        with open(output_path, 'w') as output_file:
            if compressed:
                writer = csv.writer(output_file, delimiter=',', quotechar="*")
                writer.writerow(['uuid_gender_mass'])
                short_gender = {'male': 'M', 'female': 'F'}
                for data in ret:
                    mass = data['mass'].split(' ')
                    fixed_mass = float(mass[0]) * prefix[mass[1]]
                    writer.writerow(['{}_{}_{}'.format(data['id'], short_gender[data['gender']], '%.3e' % Decimal(
                        fixed_mass))])
            else:
                writer = csv.DictWriter(output_file, fieldnames=header)
                writer.writeheader()
                writer.writerows(ret)


if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
