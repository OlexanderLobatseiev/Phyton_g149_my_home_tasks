А = int(input('А = '))
Б = int(input('Б = '))
В = int(input('В = '))

if А < Б:
    print('no good', 'А < Б')
    if А > Б:
        print('good', 'А < Б')
elif А == Б:
    if В > Б:
        print('very good', 'В > Б')
else:
    print('bad', 'Б < В')
