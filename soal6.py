import re
import secrets
import string

def extract_emails(teks):
    return re.findall(r'\S+@\S+', teks)

def generate_password(length=8):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    teks = """
    Berikut adalah daftar email dan nama pengguna dari mailing list:
    anton@mail.com dimiliki oleh antonius
    budi@gmail.co.id dimiliki oleh budi anwari
    slamet@getnada.com dimiliki oleh slamet slumut
    matahari@tokopedia.com dimiliki oleh toko matahari
    """
    
    emails = extract_emails(teks)
    for email in emails:
        username = email.split('@')[0]
        password = generate_password()
        print(f"{email} -> username: {username} , password: {password}")

if __name__ == "__main__":
    main()
