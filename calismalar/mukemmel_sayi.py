
sayi = int(input('Mükemmel sayı kontrolu yapılacak sayı: '))

bolenler = []
for i in range(1, sayi):
    if sayi % i == 0:
        bolenler.append(i)
if sum(bolenler) == sayi:
    print(f'{sayi} bir mükemmel sayıdır.')
else:
    print(f'{sayi} mükemmel sayı değildir.')