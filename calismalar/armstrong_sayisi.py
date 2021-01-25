sayi = input('Bir sayı giriniz: ')


kac_basamak = len(sayi)

toplam = 0
for i in range(kac_basamak):
    toplam += int(sayi[i]) ** kac_basamak

if toplam == int(sayi):
    print(f'{sayi} bir Armstrong sayısıdır.')
else:
    print(f'{sayi} Armstrong sayısı değildir.')