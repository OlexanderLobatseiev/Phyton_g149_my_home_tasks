А = int(input('А = '))
Б = int(input('Б = '))
В = int(input('В = '))

while А < Б:
    А += В
    if А > В:
        print(А)