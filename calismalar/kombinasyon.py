from itertools import permutations

print('Lütfen üç sayı giriniz: ')
while True:
    birinciSayi = int(input('1. >>>'))
    ikinciSayi = int(input('2. >>>'))
    ucuncuSayi = int(input('3. >>>'))
    break

kombinasyon = permutations([birinciSayi, ikinciSayi, ucuncuSayi], 2)
for i in list(kombinasyon):
    print(i)