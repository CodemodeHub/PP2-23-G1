import os

path = os.getcwd()
dir_name = input("Enter directory name: ")

os.mkdir(f'{path}/{dir_name}')