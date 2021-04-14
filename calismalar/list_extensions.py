import os

def find_extension(directory_path):
    directory = os.listdir(directory_path)
    files = []
    for file in directory:
        if file.__contains__('.'):
            if not file.startswith('.'):
                files.append(file)
                extension = file.split('.')[-1]
            return f'Extension of file is: {extension}'


while True:
    # extension = input()
    print(find_extension('/home/ftechlabs/'))