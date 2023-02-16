import os

try:
    path1 = "/Users/AlikhanGubayev/Desktop/Programming/Python/Codemode/lesson-08-16.02"
    myDir = input()
    os.chdir(f'{path1}/{myDir}')
    print("success")
except Exception as e:
    print("unknown directory")