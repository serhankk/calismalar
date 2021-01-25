
vize1 = int(input('Birinci vize notunuzu giriniz: '))
vize2 = int(input('İkinci vize notunuzu giriniz:'))
final = int(input('Final notunuzu giriniz: '))

ortalama = ((vize1 * 30) / 100) + ((vize2 * 30) / 100) + ((final * 40) / 100)
print(f'Ortalamanız: {ortalama}')