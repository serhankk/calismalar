
yazi = input('Bir yazı giriniz: ')
harfSayaci = dict()
for i in yazi:
    sayac = yazi.count(i)
    harfSayaci.update([(i, sayac)])

print(harfSayaci)