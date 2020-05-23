"""
скрипт для удаления буквы Е в имени файла фотографии, отредактированной на айфоне встроенными средствами.
Оригинальные фото помещаются в папку old 

Пример:
было IMG_E0366.JPG станет IMG_0366.JPG, а файл IMG_0366.JPG (если он был) уйдет в папку old

"""
import os
from os import path
import re


def main():
    listOfFiles = os.listdir()
    os.mkdir('old')
    for photo in listOfFiles:
        if 'E' in photo:
            new_name = str(photo[:4]) + str(photo[-8::])
            old_name = "old/" + str(new_name[:8]) + '_old' + str(new_name[-4::])
            if new_name in listOfFiles:
                os.rename(new_name, old_name)
                os.rename(photo, new_name)
            else:
                os.rename(photo, new_name)

if __name__ == "__main__":
    main()
