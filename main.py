'''import bcrypt

<strong># store your password</strong>:
password = str(input("input password: "))

<strong># Encode the stored password</strong>:
password = password.encode('utf-8')

<strong># Encrypt the stored pasword</strong>:
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

<strong># Create an authenticating password input field to check if a user enters the correct password</strong>
check = str(input("check password: "))

<strong># Encode the authenticating password as well</strong>
check = check.encode('utf-8')

<strong># Use conditions to compare the authenticating password with the stored one</strong>:
if bcrypt.checkpw(check, hashed):
    print("login success")
else:
    print("incorrect password")'''


import bcrypt


def write_pass_file(pwd):
    with open('C:\\Users\\dady\\PycharmProjects\\Contractor\\passtest.txt', 'w') as f:
        f.write(str(pwd))


def encrypt(password):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    return hashed

def check(passen):



pawss = input('pass: ')

stren = encrypt(pawss)
write_pass_file(stren)

check(input('check pass: '))




