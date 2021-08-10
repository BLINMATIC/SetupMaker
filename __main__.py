import os

def create(path, name):
    setup = open(name + '-setup.py', 'w')
    setup.write('''#SETUP MAKER
import os

print("Setup for Program ''' + name + '''")
print("Enter the path to create the program at")
path = input("> ")

os.mkdir(path)
os.chdir(path)

''')
    setup.write('print("F> ' + path + '")\n\n')
    setup.write('os.mkdir("./' + path + '")\n\n')
    setup.close()

    setup = open(name + '-setup.py', 'a')

    for root, dirs, files in os.walk(path, topdown=True):
        for name in dirs:
            print(os.path.join(root, name).replace('\\', '/'))
            setup.write('print("F> ' + os.path.join(root, name).replace('\\', '/') + '")\n\n')
            setup.write('os.mkdir("./' + os.path.join(root, name).replace('\\', '/') + '")\n\n')
        for name in files:
            print(os.path.join(root, name).replace('\\', '/'))
            try:
                File = open(os.path.join(root, name), 'r')
                setup.write('print("S> ' + os.path.join(root, name).replace('\\', '/') + '")\n\n')
                setup.write('File = open("./' + os.path.join(root, name).replace('\\', '/') + '", "w").write("""' + File.read() + '""")\n\n\n')
            except:
                File = open(os.path.join(root, name), 'rb')
                setup.write('print("B> ' + os.path.join(root, name).replace('\\', '/') + '")\n\n')
                setup.write('File = open("./' + os.path.join(root, name).replace('\\', '/') + '", "wb").write(b"""' + str(File.read()) + '""")\n\n\n')
    setup.write('''print("installation complete")
input()''')

print('Enter the folder name')
FolderName = input('> ')

print('Enter the program name')
PackageName = input('> ')

create(FolderName, PackageName)