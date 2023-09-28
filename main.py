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
import os
import json


def write_pass_file(pwd):
    path = 'assets/secret.json'
    if os.path.isfile(path):
        f = open(path)
        data = json.load(f)
        return data
    pwd = pwd.decode()
    dict = {}
    dict['password'] = pwd
    js_object = json.dumps(dict, indent=4)
    with open('assets/secret.json', 'w') as f:
        f.write(js_object)




def encrypt(password):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    return hashed

def check(passen, stren):
    check = passen.encode('utf-8')
    if bcrypt.checkpw(check, stren):
        print('OK')
    else:
        print('FALSE')


pawss = input('pass: ')

stren = encrypt(pawss)
write_pass_file(stren)

check(input('check pass: '), stren)




