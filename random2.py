import re 
password = "PasSsword4455"
kontrol = 0
while True:   
    if (len(password)<8): #8 digit control
        kontrol = -1
        break
    elif not re.search("[a-z]", password): # lower case control
        kontrol = -1
        break
    elif not re.search("[A-Z]", password): # upper
        kontrol = -1
        break
    elif not re.search("[0-9]", password): #numeric control
        kontrol = -1
        break
    elif re.search("\s", password): #space 
        kontrol = -1
        break
    else: 
        kontrol = 0
        print("geçerli parola") 
        break
  
if kontrol ==-1: 
    print("Geçersiz parola") 