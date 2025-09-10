#!/bin/sh
set -e

# 1. Jalankan proses server Ollama di latar belakang.
/bin/ollama serve &

# Ambil PID (Process ID) dari proses yang baru saja dijalankan
pid=$!

echo "Ollama server started with PID: $pid"

# 2. Tunggu beberapa detik untuk memastikan server siap menerima koneksi.
sleep 5

echo "Pulling model deepseek-r1:7b..."

# 3. Jalankan perintah pull. Ini akan berjalan sekali saat kontainer pertama kali dibuat.
#    Kita menambahkan '|| true' agar jika model sudah ada, skrip tidak akan gagal.
ollama pull deepseek-r1:7b || true

echo "Model pull command finished. Keeping server in foreground."

# 4. Tunggu proses server di latar belakang selesai (yang mana tidak akan pernah,
#    sehingga kontainer tetap berjalan).
wait $pid