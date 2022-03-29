import math
import time


def odev_1():
    print("Karşımızda rastgele dağılmış 10 insanın olduğunu düşünelim. Daha sonra bu insanları boylarına göre "
          "sıralayalım. Bu sıralamayı yapmak basit olsa da bu durumdan eski dağınık hallerine dönmek zordur.\n"
          "Kriptoloji için düşünelim. Elimizde rakamlar ve her rakamın kullanıldığı bir kod olsun. "
          "Karşımızdakine rakamların seçtiğimiz sıralama algoritmasına göre sıralanmış halini verelim.\n"
          "Bu sıralı kodu public key gibi düşünebiliriz. Karşı taraf sadece elimizdeki rakamları bilerek tüm kodu "
          "çözmeye çalışacaktır.\n")


def prime_check(num):  # 2 basamaklı asal sayı kontrolü
    for i in range(2, num):
        if (num % i) == 0 or int(math.log10(num)) + 1 != 2:
            return False
    return True


def odev_2():  # Verilen sayıların çarpımlarını ve sonra bu çarpımın çarpanlarını bulan kod parçası
    a = 789999983
    b = 789999989
    ab = a * b
    print(f"Multipication of numbers: {ab}")
    c = []

    start = time.time()

    i = 1
    while i * i <= ab:  # Sayının çarpanları kareköküne kadar hesaplanır. Sayının karekökü çarpanların orta noktası olacaktır.
        if ab % i == 0:
            c.append(i)
            c.append(int(ab / i))
        i += 1

    end = time.time()
    print("Factors of Multipication:", c)
    print(end - start, "seconds\n")


def odev_3():
    check_p = False
    check_q = False

    while not check_p:
        p = int(input("Enter a 2-digit and prime number for p: "))
        check_p = prime_check(p)

    while not check_q:
        q = int(input("Enter a 2-digit prime number for q other than p: "))
        if p != q:
            check_q = prime_check(q)

    n = p * q
    print("Modulus number is: ", n)

    to = (p - 1) * (q - 1)
    print("Eulers Toitent (φ) is: ", to)

    e = int(input(f"Enter a 2-digit number that is coprime with {to} for e: "))

    while math.gcd(e, to) != 1 or not (1 < e < to):  # e sayısı için ek kontroller yapıldı.
        e = int(input(f"Enter a 2-digit number that is coprime with {to} for e: "))

    pri_key = 0

    for i in range(2, to):  # private key bulundu (d).
        if (e * i) % to == 1:
            pri_key = i
            break

    mes = int(input("Enter your message number: "))

    enc = mes ** e % n
    print("Encrypted number is:", enc)

    print("Private key is:", pri_key)

    dec = enc ** pri_key % n
    print("Decrypted number is:", dec)


if __name__ == "__main__":
    odev_1()
    odev_2()
    odev_3()
