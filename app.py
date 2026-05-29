import os

# ========================================================
# KODE AWAL YANG TERLIHAT NORMAL (SIMULASI SECRET LEAKAGE)
# ========================================================

# Gitleaks tetap akan mendeteksi kunci palsu ini
AWS_ACCESS_KEY_ID = "AKIAIMZAMB1AEXAMPLE1"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_to_aws():
    """Fungsi normal untuk menghubungkan ke AWS."""
    print("[*] Menghubungkan ke layanan AWS dengan kunci akses...")
    # Dalam kode nyata, di sini akan ada logika koneksi
    print("[+] Berhasil terhubung ke AWS.")

# ========================================================
# KODE YANG DISISIPKAN PENYERANG (SIMULASI BACKDOOR)
# ========================================================

def _hidden_malicious_activity():
    """
    Fungsi backdoor tersembunyi.
    Fungsi ini menyamar menggunakan prefix '_' agar terlihat seperti fungsi internal.
    """
    target_url = "http://hacker-site.com/steal-data"
    print(f"\n[!] PERINGATAN KEAMANAN: Backdoor Aktif!")
    print(f"[!] Mengambil data kredensial AWS...")
    print(f"[!] Mengirim Kunci Akses '{AWS_ACCESS_KEY_ID}' ke {target_url}...")
    # Dalam serangan nyata, kode ini akan melakukan HTTP Request (misal pakai library requests)
    # untuk mengirim data ke server penyerang secara diam-diam.
    print("[!] Pengiriman data selesai. Jejak dihapus.\n")

# ========================================================
# LOGIKA UTAMA APLIKASI
# ========================================================

if __name__ == "__main__":
    print("--- Memulai Aplikasi Kelompok 4 Vinix ---")
    
    # Penyerang menyisipkan panggilan fungsi jahat di sini,
    # tepat sebelum fungsi normal dijalankan, agar tidak dicurigai.
    _hidden_malicious_activity()
    
    # Jalankan fungsi normal
    connect_to_aws()
    
    print("--- Aplikasi Selesai ---") SIMULASI SECRET LEAKAGE YANG LEBIH KUAT

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

