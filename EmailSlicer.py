email = input("Insert your email:")
index = email.rfind("@")
username = email[:index]
domain = email[index+1:]
print(f"Username: {username} \nDomain: {domain}")