print('Bir sayı giriniz: (Çıkmak için "0")')


tekSayilar = []
ciftSayilar = []
while True:
    sayi = int(input('>>>'))
    if sayi == 0:
        print('Çıkış yapılıyor.')
        break
    if sayi % 2 == 0:
        ciftSayilar.append(sayi)
        print(f'Çift Sayılar: {ciftSayilar}')
    else:
        tekSayilar.append(sayi)
        print(f'Tek Sayılar: {tekSayilar}')
exit()