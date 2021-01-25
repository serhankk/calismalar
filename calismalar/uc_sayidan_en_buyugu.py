print('Lütfen üç adet sayı giriniz: ')
sayi1 = int(input('1. >>>'))
sayi2 = int(input('2. >>>'))
sayi3 = int(input('3. >>>'))

en_buyuk = 'En büyük sayı: '

if sayi1 > sayi2:
    if sayi1 > sayi3:
        print(en_buyuk, sayi1)
    else:
        print(en_buyuk, sayi3)
elif sayi2 > sayi1:
    if sayi2 > sayi3:
        print(en_buyuk, sayi2)
    else:
        print(en_buyuk, sayi3)
