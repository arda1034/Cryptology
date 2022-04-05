import hashlib
import string
import random


def sign_up():  # Yeni kullanıcıyı data dosyasına ekler.
    usr = input("Please enter your username:")
    psw = input("Please enter your password:")

    with open('Database.txt', 'a+') as f:
        f.write("Username: %s\n" % usr)
        f.write(usr + "'s Password: %s" % hashlib.sha256(psw.encode('utf-8')).hexdigest() + "\n")


def login():  # Dataların bulunduğu dosyada bilgileri girilen kullanıcıyı arayarak sonuç verir.
    usr = input("Please enter your username:")
    psw = input("Please enter your password:")

    with open('Database.txt', 'r') as f:
        if (usr + "'s Password: %s" % hashlib.sha256(psw.encode('utf-8')).hexdigest()) in f.read():
            print("Access permitted.")
        else:
            print("Access denied.")


def q_1():
    ch = input("Press 1 for sign up, press 2 for login, and press a different key for exit:")
    if ch == "1":
        sign_up()
    elif ch == "2":
        login()
    else:
        exit()


def q_2():  # 500 karakterli random bir stringin sırayla tüm karakterlerini değiştirerek MD5 sonuçlarını inceleme
    n = 500
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    print("String: ", res)
    print("MD5: ", hashlib.md5(res.encode()).hexdigest() + "\n")
    ind = 0

    while ind <= n - 1:
        rnd = ''.join(random.choices(string.ascii_letters + string.digits))
        if res[ind] != rnd:
            res = res[:ind] + rnd + res[ind + 1:]
            print("String: ", res)
            print("MD5: ", hashlib.md5(res.encode()).hexdigest() + "\n")
            ind = ind + 1


if __name__ == "__main__":
    q_1()
    #q_2()
