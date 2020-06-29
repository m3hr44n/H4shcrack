#python project
#mehraan kiya
#roshanamooz

import hashlib

hash_ = input("Enter the hash : ==> ")

file_pass = input("Enter The Your Password file : ==> ")

print

with open(file_pass) as f:
    for i in f:
        line = i.strip()

        if  hashlib.md5(line).hexdigest() == hash_:
         
         
            
            print("Hash Cracked ==> "),line
            
            break

        else:

            print("test : "),line