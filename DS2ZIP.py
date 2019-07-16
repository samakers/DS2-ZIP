import os
import zipfile
from colorama import *
init()

print('DS2ZIP 1.0\n')

print( Fore.RED + 'Be careful when entering the directory as any changes will apply to ALL files within. Please copy any files into a temporary location before proceeding.\n' + Fore.WHITE)

get_directory = input('Enter the directory of the .DS2 files...\n')

author_id = input('Enter a valid four digit author id...\n')

jobtype_id = input('Enter a valid job type...\n')

file_names = set()
for f in os.listdir(get_directory):
    file_name, file_ext = os.path.splitext(f) #splitting file name and extension
    file_names.add(file_name)
    path = os.path.join(get_directory, file_name + ".wst") #prepending the file name with directory
    wst_file = open(path, "w+") #creating .wst file 
    wst_file.write("[JobParameters]\nAuthorId=" + author_id + "\nJobtypeId=" + jobtype_id +"\nPriority=NORMAL\nKeyfield=\nUserfield1=\nUserfield2=\nUserfield3=\nUserfield4=\nNotes=\n")
    wst_file.close() #closing wst file

for file_name in file_names: 
    zip_file = os.path.join(get_directory, file_name + '.zip')
    with zipfile.ZipFile(zip_file, 'w') as myzip:
        member_file = os.path.join(get_directory, file_name + '.wst')
        myzip.write(member_file, file_name + '.wst')
        member_file = os.path.join(get_directory, file_name + '.DS2')
        myzip.write(member_file, file_name + '.DS2')
print( Fore.GREEN + '')
input('Zipping complete! Press any key to exit...\n')
