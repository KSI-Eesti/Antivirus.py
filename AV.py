#import all libraries for this code
#like operating system, hashlib to convert code into hexadecimal
#time to be used as a timer

import os, sys, time, hashlib
file_list = []
root_dir = "/home/cesar/Documents/Bootstrap v.5 "
print("Start scan...")
#going through all directories in root directory
#looking for all suspicious files
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = subdir + os.sep + file

        if(file_path.endswith(".exe") or file_path.endswith(".bat")):
            file_list.append(file_path)

print("we found some suspicious files")
print("start scan files")
def counts():
    for x in range(5):
        print(x+1)
        time.sleep(1)
counts()


#the scan function
#all files in the file list are opened and compared to the virus definition
#the virus definition(virus_def) is opened and used as reference
#after detection the user can choose to delete the files or ignore the threat
def scan():
    Y = "Yes"
    N = "No"
    infected_list = []
    for fi in file_list :
        virus_def = open("viruses.txt", "r")
        file_not_read = False
        print("\n scanning... : ()".format(fi))
        hashe = hashlib.sha256()
        try:
            file = open(fi, "rb").read()
            try:
                    buf = file
                    file_not_read = True
                    s = bytes(buf, 'utf-16')
                    hashe.update(s)
                    file_hashed == hashe.hexdigest()
                    print("file encrypted with sha256:{}".format(file.hashed))
                    for line in virus_def :
                        if file_hashed == line.strip():
                            print("Malware detected --> file named:{}".format(fi))
                            infected_list.append(fi)
                        else:
                            pass
            except Exception as e:
             print("could not read the file, Error: ()".format(e))
        except:
            pass
    print("Infected files found : ()".format(infected_list))
    deleteOrnot = str(input("Would you like to solve these issues Y = Yes N= No (Y/N)"))
    if deleteOrnot.upper() == Y:
        for infect in infected_list:
            os.remove(infect)
            print("file removed, issue resolved : {}".format(infect))
    else:
        print("Your issues have been solved succesfully ...")
        os.system("PAUSE")
     



    scan();
                    
                    
                    
