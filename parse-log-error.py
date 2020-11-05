import os
import re
import time

# Funkcje
def fileList(source):
   matches = []
   for root, dirnames, filenames in os.walk(source):
       for filename in filter(lambda name:pattern.match(name),filenames):
           matches.append(os.path.join(root, filename))
           #print(matches)
   return matches

# Zmienne
pattern = re.compile('.*\.(log|txt)$')
checks = fileList('/var/log/')
os.remove("err_log.txt")
err_file = open("err_log.txt","a+")

# Program
for check in checks:
    try:
        f = open(check)
        lines = f.readlines()
        for line in lines:
            #print(line.split() [2], line.split() [5]
            if 'error' in line:
                print(line.split())
                err_file.write(str(line.split()))
                err_file.write('\n')
    except IOError:
            print('Brak dostępy do pliku : {} '.format(check))
err_file.close()
