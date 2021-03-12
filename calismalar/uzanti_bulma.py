
def find_extention(file):
    if file.__contains__('.'):
        extention = file.split('.')[-1]
        return f'Dosyanın uzantısı: {extention}'
    else:
        return 'Uzantı bulunamadı.'
