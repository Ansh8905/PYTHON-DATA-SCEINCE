from datetime import datetime
from genericpath import isdir, isfile
import os

from numpy import size


#create folder
if os.path.exists('test'):
    print('test folder exists')
else:
    os.mkdir('test')
    print('test folder created')

#create a folder path
folder = ' a/b/c/d/e/f/g'
if os.path.exists(folder):
    print('path exists')
else:
    os.makedirs(folder)
    print('print created')


#delete file
if os.path.exists('faltu.txt'):
    os.unlink('faltu.txt')
    print('faltu.txt deleted')
else:
    print('faltu.txt does not exist')

    #delete a folder........
if os.path.exists('test'):
    os.rmdir('test')
    print('tests folder deleted')
else:
    print('tets folder does not exist')


#display file details 
if os.path.exists('Basics/hello.py'):
    size = os.path.getsize('Basics/hello.py')
    ctime = os.path.getctime('Basics/hello.py')
    mtime = os.path.getmtime('Basics/hello.py')
    isfile = os.path.isfile('Basics/hello.py')
    isdir = os.path.isdir('Basics/hello.py')
print('filename:Basics/hello.py')
print('size:', size,'bytes')
print('ctime:', datetime.fromtimestamp(ctime))
print('mtime:', datetime.fromtimestamp(mtime))
print('file h ye?:',isfile)
print('file h ye?:',isdir)

#recursive display file tree

print("recursuve display file tree")
for root, dirs, files in os.walk('.'):
    print(f"folder is{root.upper()}")
    print("total folders:",len(dirs))
    print("files in this folders are:",files)