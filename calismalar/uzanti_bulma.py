dosya = input('Dosya adı giriniz: ')

if dosya.__contains__('.'):
    uzanti = dosya.split('.')[-1]
    print(f'Dosyanın uzantısı: {uzanti}')
else:
    print('Uzantı bulunamadı.')