# basic hacking simulation
import base64
import time

password = "key"

def startingpoint():
    asker = input("Please Enter The Password: ")
    if asker == password:
        print("Checking...")
        time.sleep(1)
        print("password looks good!")
        time.sleep(1)
        victimpc() 
    else:
        time.sleep(1)
        print("password is wrong!")




def victimpc():
    while True:
        user = input("Martin@Jorge: ")
        emails = 'emails.txt'
        bank = 'bankpass.txt'
        flag = 'flag.txt'
        if user == 'ls':
            print(emails, bank, flag)
        elif user == 'cat ' + bank:
            print("brok33")
        elif user == 'cat ' + emails:
            print("unhackable-password!")
        elif user == 'cat ' + flag:
            print("c0ngr4tz!!")
        elif user == 'exit':
            break
    

startingpoint()










































