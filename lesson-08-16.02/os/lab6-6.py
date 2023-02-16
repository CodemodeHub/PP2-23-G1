import os

# создаем папку 
os.mkdir(f'{os.getcwd()}/alphabet')

# меняем directory
os.chdir(f'{os.getcwd()}/alphabet')

try:
    for i in range(65, 91):
        open(chr(i) + '.txt', 'w')
except Exception as e:
    print(f'Error: {e}')