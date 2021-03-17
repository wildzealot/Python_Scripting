import os
import hashlib
import zipfile


homeBase = (os.path.expandvars('%SystemRoot%'))

FILENAMES=[]
#The desired directory needs to be input here other wise it will just use the ROOT directory
#list all folders and files in a directory
#store all files with a certain extension in one list
for root, dirs, files in os.walk(homeBase):
    for filename in files:
        #the file extension needs to be changed depending upon desired file type
        if(filename.endswith('.txt')):
            FILENAMES.append(filename)
            # this prevents the entire file from being written to memory
            BLOCKSIZE = 65536
            hasher = hashlib.sha256()
            try:
                with open(root+ '\\' + filename, 'rb') as afile:
                    buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher.update(buf)
                        buf = afile.read(BLOCKSIZE)
                    results = open('CDI_HASHES.txt', 'a')
                    results.write('The file is located in ' + root + '\\' + "\n") 
                    results.write('the SHA256 hash for ' + filename + ' is: ' + hasher.hexdigest() + "\n")
                    results.close() 
            except PermissionError:
                '[Errno 13] Permission denied:'  

print('\n')
#Zip the resulting collected file of hashes
with zipfile.ZipFile('CDI_HASHES.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('CDI_HASHES.txt')
    
#remove the created text file
os.remove('CDI_HASHES.txt')
print('''

The text file has been Removed!

Please send the CDI_HASHES.zip file to CyberDefenses via Sharefile.

Thank you for your assistance!

''')
#Write a script to search the output for known bad hashes