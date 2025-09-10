# Dockerfile (Diperbarui)

# 1. Gunakan image Python resmi sebagai dasar
FROM python:3.11-slim

# 2. Set environment variables untuk Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- BLOK BARU: INSTAL DEPENDENSI LEVEL SISTEM OPERASI ---
# Perbarui package manager dan instal GDAL library.
# - build-essential diperlukan oleh beberapa pustaka Python untuk kompilasi.
# - libgdal-dev adalah library utama GDAL yang dicari oleh Django.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libgdal-dev \
    # Bersihkan cache untuk menjaga ukuran image tetap kecil
    && rm -rf /var/lib/apt/lists/*
# --- AKHIR BLOK BARU ---

# 3. Buat direktori kerja di dalam kontainer
WORKDIR /app

# 4. Salin file requirements.txt terlebih dahulu
COPY requirements.txt .

# 5. Instal semua dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. Salin seluruh kode proyek ke dalam direktori kerja
COPY . .

# 7. Port yang akan diekspos oleh kontainer (port internal)
EXPOSE 8000

# 8. Perintah default untuk menjalankan aplikasi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]