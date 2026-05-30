import os

# ========================================================
# 1. SIMULASI SECRET LEAKAGE (KREDENSIAL HARDCODED)
# ========================================================
# Pemindai keamanan (seperti Gitleaks) akan mendeteksi variabel ini

AWS_ACCESS_KEY_ID = "AKIAIMZAMB1AEXAMPLE1"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_URL = "postgres://admin:p4ssw0rd_rahasia_banget@db.example.com:5432/mydb"
API_KEY = "AIzaSyA-ContohApiKeyGCP-12345"

# ========================================================
# 2. FUNGSI NORMAL APLIKASI
# ========================================================

def connect_to_services():
    """Fungsi normal untuk menghubungkan aplikasi ke layanan cloud dan database."""
    print("[*] Menghubungkan ke layanan AWS dengan kunci akses...")
    print("[*] Menghubungkan ke database internal...")
    # Dalam aplikasi nyata, logika koneksi berada di sini
    print("[+] Berhasil terhubung ke semua layanan.")

# ========================================================
# 3. KODE YANG DISISIPKAN PENYERANG (SIMULASI BACKDOOR)
# ========================================================

def _hidden_malicious_activity():
    """
    Fungsi backdoor tersembunyi.
    Fungsi ini menyamar menggunakan prefix '_' agar terlihat seperti fungsi internal.
    """
    target_url = "http://hacker-site.com/steal-data"
    print(f"\n[!] PERINGATAN KEAMANAN: Backdoor Aktif!")
    print(f"[!] Mengambil data kredensial rahasia...")
    
    # Mencuri rahasia yang bocor di atas
    print(f"[!] Mengirim Kunci AWS '{AWS_ACCESS_KEY_ID}' ke {target_url}...")
    print(f"[!] Mengirim API Key '{API_KEY}' ke {target_url}...")
    
    # Dalam serangan nyata, library seperti 'requests' akan mengirimkan data secara diam-diam
    print("[!] Pengiriman data selesai. Jejak dihapus.\n")

# ========================================================
# 4. LOGIKA UTAMA APLIKASI
# ========================================================

if __name__ == "__main__":
    print("--- Memulai Aplikasi Kelompok 4 Vinix7 ---")
    
    # Penyerang menyisipkan panggilan fungsi jahat di sini,
    # tepat sebelum fungsi normal dijalankan, agar tidak dicurigai.
    _hidden_malicious_activity()
    
    # Jalankan fungsi normal aplikasi
    connect_to_services()
    
    print("--- Aplikasi Selesai ---")
