#!/bin/sh

# Jalankan migrasi database Django untuk memastikan skema database terbaru
echo "Applying database migrations..."
python manage.py migrate --noinput

# Jalankan Gunicorn web server
echo "Starting Gunicorn..."
gunicorn core.wsgi:application -c gunicorn.conf.py