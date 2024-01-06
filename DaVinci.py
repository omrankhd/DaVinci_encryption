import os
import sys
from cryptography.fernet import Fernet

yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n'])
G = '\033[92m' #green
Y = '\033[93m' #yellow
B = '\033[94m' #blue
R = '\033[91m' #red
W = '\033[0m' #white
def banner():
    print ("""

%s
  _____     __      ___            _ 
 |  __ \    \ \    / (_)          (_)
 | |  | | __ \ \  / / _ _ __   ___ _ 
 | |  | |/ _` \ \/ / | | '_ \ / __| |
 | |__| | (_| |\  /  | | | | | (__| |
 |_____/ \__,_| \/   |_|_| |_|\___|_|                                       
                                         __  _         
             ___ ___  __________ _____  / /_(_)__  ___ 
            / -_) _ \/ __/ __/ // / _ \/ __/ / _ \/ _ \_
            \__/_//_/\__/_/  \_, / .__/\__/_/\___/_//_/
                            /___/_/                                                       
   %s

                      
                        [+] Created By omran_khadraoui [+]


%s
encryption/decreption method(choose a methode):

 1) AES
 2) DES
 3) RSA
 0) Exit
"""%(R,G,B))

    
    banner = input(" Select from the menu : ")

    if banner == "1":
	        AES()
    elif banner == "2":
	        print("")
    elif banner == "3":
	        print("3")
    else:
        sys.exit(); 
def AES():
    print ("do you want to encrypt or decrypt ?")
    print("""
  1) encrypt
  2) decrypt
""")
    AESm = input ("select encrypt or decrypt : ")
    if AESm == "1":
        whattoencrypt()
    elif AESm == "2":
        whattodecrypt()
    else:
        banner()
    ####################################################
def whattoencrypt(msg =""):
      print ("what do you want to encrypt ?")
      print("""
  1) a folder containing files
  2) a single file
  3) just a message
""")
      w = input (f"select what do you want to encrypt : {msg}")
      if w == "1":
            whatfolderenc()
      if w == "2":
            fileencrypt()
      if w == "3":
            messageenc()
      else :
            whattoencrypt("enter a valid option : ")
    ####################################################nnnnnnnnnnnn
def whattodecrypt(msg=""):
      print ("what do you want to decrypt ?")
      print("""
  1) a folder containing files
  2) a single file
  3) just a message
""")
      w = input (f"select what do you want to decrypt : {msg}")
      if w == "1":
            whatfolderdec()
      if w == "2":
            filedecrypt()
      if w == "3":
            messagedec()
      else :
            whattodecrypt("enter a valid option : ")
     ####################################################        nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
def whatfolderenc():
    path= input("enter full folder path(press Enter for current folder) : ")
    if path== "":
        thisfolderencrypt()
    else:
        folderencrypt(path)

def whatfolderdec():
    path= input("enter full folder path(press Enter for current folder) : ")
    if path=="":
        thisfolderdecrypt()
    else:
        folderdecrypt(path)

 ####################################################
def thisfolderencrypt():
    files = []
    for file in os.listdir():
            if file == "DaVinci.py" or file == "mykey.key" or file == "mymessagekey.key" or file == "myfilekey.key":
                    continue
            if os.path.isfile(file):
                    files.append(file)
    key = Fernet.generate_key()

    with open("mykey.key","wb") as thekey:
           thekey.write(key)
    
    for file in files:
            with open(file, 'rb') as thefile :
                  contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file,"wb") as thefile :
                  thefile.write(contents_encrypted)
    print("folder files encrypted")
    sys.exit()
  ####################################################       
def folderencrypt(path):
    exclude_files = ['DaVinci.py', 'mykey.key','mymessagekey.key','myfilekey.key']
    files = [os.path.join(os.path.abspath(path), x) for x in os.listdir(path) if x not in exclude_files]
    
    key = Fernet.generate_key()

    with open("mykey.key","wb") as thekey:
           thekey.write(key)
    
    for file in files:
            with open(file, 'rb') as thefile :
                  contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file,"wb") as thefile :
                  thefile.write(contents_encrypted)
    print("folder files encrypted")
    sys.exit()
 ####################################################
def thisfolderdecrypt():
    files = []
    for file in os.listdir():
            if file == "DaVinci.py" or file == "mykey.key" or file == "mymessagekey.key":
                    continue
            if os.path.isfile(file):
                    files.append(file)
    
    keyfile = input ("enter a key file (press enter if you have a file named myfilekey.key)")
    if keyfile == "":
            with open("mykey.key","rb") as thekey:
                secretkey = thekey.read()
    else:
            with open(keyfile,"rb") as thekey:
                secretkey = thekey.read()
    
    passphrase="omran"
    user_phrase= input("enter the password to decrypt your files : ")
    if user_phrase == passphrase:
        for file in files:
            with open(file, 'rb') as thefile :
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file,"wb") as thefile :
                thefile.write(contents_decrypted)
    print("folder files decrypted")
    sys.exit()
   ####################################################              
def folderdecrypt(path):
    exclude_files = ['DaVinci.py', 'mykey.key','mymessagekey.key','myfilekey.key']
    files = [os.path.join(os.path.abspath(path), x) for x in os.listdir(path) if x not in exclude_files]
    keyfile = input ("enter a key file (press enter if you have a file named mykey.key)")
    if keyfile == "":
            with open("mykey.key","rb") as thekey:
                secretkey = thekey.read()
    else:
            with open(keyfile,"rb") as thekey:
                secretkey = thekey.read()
    
    passphrase="omran"
    user_phrase= input("enter the password to decrypt your files : ")
    if user_phrase == passphrase:
        for file in files:
            with open(file, 'rb') as thefile :
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file,"wb") as thefile :
                thefile.write(contents_decrypted)
    print("folder files decrypted")
    sys.exit()

def fileencrypt():
     
    file = input("enter file name in this folder to encrypt : ")
    
    if file == "DaVinci.py" or file == "mykey.key" :
        print("you can't encrypt this file")
        sys.exit()
    if os.path.isfile(file):
        key = Fernet.generate_key()
    else:
          print ("not a file")    
          sys.exit()

    with open("myfilekey.key","wb") as thekey:
           thekey.write(key)
    
   
    with open(file, 'rb') as thefile :
         contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile :
         thefile.write(contents_encrypted)
    print("file encrypted")
    sys.exit()
#################################################
def filedecrypt():
    file = input("enter file name in this folder to decrypt : ")
    
    if file == "DaVinci.py" or file == "mykey.key" or file =="myfilekey.key" :
        print("you can't decrypt this file")
        sys.exit()
    if os.path.isfile(file):
      print("")  
    else:
          print ("not a file")    
          sys.exit()
    keyfile = input ("enter a key file (press enter if you have a file named myfilekey.key)")
    if keyfile == "":
            with open("myfilekey.key","rb") as thekey:
                secretkey = thekey.read()
    else:
            with open(keyfile,"rb") as thekey:
                secretkey = thekey.read()
    
    passphrase="omran"
    user_phrase= input("enter the password to decrypt your files : ")
    if user_phrase == passphrase:
            with open(file, 'rb') as thefile :
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file,"wb") as thefile :
                thefile.write(contents_decrypted)
    print("file decrypted")
    sys.exit()
##################################################
def messageenc():
    message = input("write a message to incrypt : ")
    b = bytes(message, 'utf-8')
    key = Fernet.generate_key()
    with open("mymessagekey.key","wb") as thekey:
           thekey.write(key)
    message_encrypted = Fernet(key).encrypt(b)
    with open("your_encrypted_message.txt","wb") as themessageencrypted:
           themessageencrypted.write(message_encrypted)
    print("message encrypted and saved in your_encrypted_message.txt")
    print(message_encrypted)
    sys.exit()
##################################################
def messagedec():
    message = input("write a message to derypt or enter a file name (you must have a file named mymessagekey.key contains the decryption key ) : ")
    b = bytes(message, 'utf-8')
    keyfile = input ("enter a key file (press enter if you have a file named mymessagekey.key)")
    if keyfile == "":
            with open("mymessagekey.key","rb") as thekey:
                secretkey = thekey.read()
    else:
            with open(keyfile,"rb") as thekey:
                secretkey = thekey.read()
    
    if os.path.isfile(message):
            passphrase="omran"
            user_phrase= input("enter the password to decrypt your files : ")
            if user_phrase == passphrase:
                with open(message, 'rb') as thefile :
                    contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open("your_decrypted_message.txt","wb") as thefile :
                thefile.write(contents_decrypted)
    else:
        passphrase="omran"
        user_phrase= input("enter the password to decrypt your files : ")
        if user_phrase == passphrase:
            message_decrypted = Fernet(secretkey).decrypt(b)
            with open("your_decrypted_message.txt","wb") as themessagedecrypted:
                themessagedecrypted.write(message_decrypted)
            print(message_decrypted)
    print("message decrypted and saved in your_decrypted_message.txt")
    sys.exit()
if __name__ == "__main__":
    banner()
