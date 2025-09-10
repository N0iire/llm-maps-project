# ollama/Dockerfile (Diperbarui)

# Mulai dari image Ollama resmi
FROM ollama/ollama

# Salin skrip entrypoint kita ke dalam image
COPY entrypoint.sh /entrypoint.sh

# Jadikan skrip tersebut dapat dieksekusi
RUN chmod +x /entrypoint.sh

# Atur entrypoint kontainer untuk menjalankan skrip kita
ENTRYPOINT ["/entrypoint.sh"]