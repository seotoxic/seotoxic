import os
import urllib.parse

# ====== KONFIGURASI ======
DOMAIN = "https://fik.unimed.ac.id/wp-content/info/"

# ====== STEP 1: BACA keyword.txt ======
with open("keyword.txt", "r", encoding="utf-8", errors="replace") as f:
    keywords = [line.strip() for line in f if line.strip()]

# ====== STEP 2: BACA TEMPLATE HTML ======
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# ====== STEP 3: GENERATE HALAMAN ======
for brand in keywords:
    folder_name = f"sabarya-{brand}"
    os.makedirs(folder_name, exist_ok=True)

    # Ganti konten
    html_content = template.replace("{{BRAND}}", brand.upper())
    html_content = html_content.replace("{{DOMAIN}}", f"{DOMAIN}?sabarya={brand}")

    # Simpan index.html
    with open(os.path.join(folder_name, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

print("✅ Semua halaman berhasil dibuat. Canonical pakai ?sabarya=xxx.")
