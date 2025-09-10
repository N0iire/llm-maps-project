# gunicorn.conf.py

# Alamat dan port yang akan didengarkan oleh Gunicorn
bind = "0.0.0.0:8000"

# Jumlah worker processes. Aturan umumnya adalah (2 * jumlah_cpu) + 1
# Kita akan menggunakan 3 sebagai default yang aman.
workers = 3

# Tipe worker (sync adalah default dan paling kompatibel)
worker_class = "sync"

# Waktu timeout untuk worker (dalam detik)
timeout = 30

# Level logging
loglevel = "info"