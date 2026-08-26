name = input("Insert username:")
flag = False
if(len(name)<=20):
 for x in range(0,len(name)-1):
    if(name[x].isalpha()== False and name[x].isdigit()==False):
       print("User name should only contain numbers and alphabets.")
       print(f"{name[x]} can't be accepted.")
       flag=True
       break
    
else:
    print("Username needs to be less than 20 characters.")
if flag==False:
   print(f"Welcome {name}")