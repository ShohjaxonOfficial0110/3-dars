import random
def generate_password(length = int(input("Raqam kiriting: "))): 
    Kichik_harf = "abdeghijklmnopqrstuvxyzo'g'shchng" 
    Katta_harf = "ABDEGHIJKLMNOPQRSTUVXYZO'G'SHCHNG"
    Raqamlar="123456789"
    Simvollar = "!@#$%^&*()_+"
    all_chars = Kichik_harf + Katta_harf + Raqamlar + Simvollar
    password_chars = random. sample(all_chars, length)
    password = "". join(password_chars)

    return password

password = generate_password()
print(password)