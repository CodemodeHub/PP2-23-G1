import os

path = os.getcwd()
os.chdir(f'{path}/Codemode')
path = os.getcwd()

arr = os.listdir(path)

txt_file = ""
for i in arr:
    if os.path.isfile(i):
        txt_file = i

lines_cnt = 0
with open(f'{path}/{txt_file}', 'r') as file:
    for line in file:
        if line != "\n":
            lines_cnt += 1

print(lines_cnt)