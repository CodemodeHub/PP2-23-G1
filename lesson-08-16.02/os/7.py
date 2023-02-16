import os

path = os.getcwd()
# print(path)

os.chdir(f'{path}/Codemode')

# print(os.getcwd())
path = os.getcwd()

# print(os.listdir(path))
for i in os.listdir(path):
    if os.path.isdir(i):
        print(f'<DIR> : {i}')
    elif os.path.isfile(i):
        print(f'<FILE> : {i}')
