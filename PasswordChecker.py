password = input("Enter password:")
Alpha=False
Num=False
Char= False
for x in range(0,len(password)-1):
    if(password[x].isalpha() == True):
        Alpha= True
    elif password[x].isdigit() == True:
        Num=True
    else:
        Char=True
if(Char==True and Alpha==True and Num==True):
    print(f"{password} is a strong password.")
else:
    print("Weak Password")