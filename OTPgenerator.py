elements = {"1","2","3","4","5","6","7","8","9","0"}
flag=True
otp=[]
for x in range(5,1,-1):
 num=int(elements.pop())
 otp.append(num)
for x in otp:
 print(x,end="")
print("")
password = input("Insert OTP:")
if(len(password)>len(otp)):
 print("OTP shouldn't be  longer than 4 characters.")
 password = input("Insert OTP:")
for x in range(0,len(password)):
 if int(password[x]) != int(otp[x]):
  print(f"{password[x],otp[x]}")
  flag=False
  print("OTP doesn't match.")
  break
if(flag==True):
 print("OTP matched.")

