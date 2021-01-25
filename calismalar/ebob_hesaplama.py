

ilkSayi = int(input('İlk sayıyı giriniz: '))
ikinciSayi = int(input('İkinci sayıyı giriniz: '))

if ilkSayi > ikinciSayi:
    buyuk = ilkSayi
else:
    buyuk = ikinciSayi

ortakBolenler = []
for i in range(1, buyuk):
    if ilkSayi % i == 0 and ikinciSayi % i == 0:
        ortakBolenler.append(i)
        ortakBolen = max(ortakBolenler)

print(ortakBolen)