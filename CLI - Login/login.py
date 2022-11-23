'''Login system:
    UserID: lizmil
    password: lizmil'''

import hashlib

#User adds a UserID and Password
usr = input("Add User name: ")
psw = input("Add a password for User name: ")

#hash input password
psw_encode = psw.encode()
sha_psw = hashlib.sha256(psw_encode).hexdigest()

#print hashed password (only for example)
print(sha_psw)

#Login validation

count_u = 0
count_p = 0

user = input("User name: ")
while True:
    if user != usr:
        count_u += 1
        if count_u == 3:
            print("You gived 3 times a wrong user name! Exit... ")
            break
        print(f"User name isn't correct. You have {3-count_u} chance left.")
        user = input("User name: ")
        
    else:
        count_u = 0
        password = input("Password: ")
        password_encode = password.encode()
        password_sha = hashlib.sha256(password_encode).hexdigest()
        print(password_sha)     #print only for checking!
        if password_sha != sha_psw:
            count_p += 1
            if count_p == 3:
                print("You gived 3 times a wrong password! Exit... ")
                break
            print(f"Wrong password. You have {3-count_p} chance left.")
            
        else:
            print("You logged in.")
            break