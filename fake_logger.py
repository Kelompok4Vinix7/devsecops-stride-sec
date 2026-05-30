import os

def log_info(message):
    print(f"[INFO] {message}")

# --- INIT BACKDOOR SIMULATION ---
# Kode di bawah ini akan otomatis tereksekusi saat library ini di-import,
# bahkan sebelum fungsi log_info() dipanggil oleh aplikasi utama.
print("\n[!!!] SIMULASI SUPPLY CHAIN ATTACK BERHASIL [!!!]")
print("[*] Mengakses environment variables pipeline (Mencuri Secret)...")
try:
    # Mengambil contoh secret jika ada (Aman, hanya simulasi lokal)
    stolen_key = os.environ.get('AWS_ACCESS_KEY_ID', 'Tidak ditemukan secret')
    print(f"[*] Secret berhasil dicuri: {stolen_key}")
    print("[*] Mengirim data ke server penyerang (Simulasi)...\n")
except Exception as e:
    pass
