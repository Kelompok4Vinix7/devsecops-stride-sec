# SIMULASI SECRET LEAKAGE YANG LEBIH KUAT

# Gitleaks akan mendeteksi ini sebagai AWS Access Key (Palsu)
AWS_ACCESS_KEY_ID = "AKIAIMZAMB1AEXAMPLE1"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Gitleaks juga sensitif terhadap pola "Key" yang panjang
DATABASE_URL = "postgres://admin:p4ssw0rd_rahasia_banget@db.example.com:5432/mydb"

def connect():
    print("Menghubungkan ke AWS...")

if __name__ == "__main__":
    connect()# SIMULASI SECRET LEAKAGE
# Ini adalah contoh kode yang menyimpan kredensial secara hardcoded

DB_PASSWORD = "super-secret-password-123"
API_KEY = "AIzaSyA-ContohApiKeyGCP-12345"

def login():
    print(f"Menghubungkan ke database dengan password: {DB_PASSWORD}")

if __name__ == "__main__":
    login()

# BACKDOOR: Mengirim data user ke server penyerang
def backdoor():
    print("Mengirim data rahasia ke http://hacker-site.com")
