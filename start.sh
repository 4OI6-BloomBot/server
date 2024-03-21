#!/bin/sh

# ==========================================
# Start script for server
# Waits for DB connection before migrating
# ==========================================
echo '[INFO] Waiting for database'

while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 0.1
done

echo '[INFO] Database ready!'


echo '[INFO] Running migrations'
python manage.py migrate
echo '[INFO] Done!'

echo '[INFO] Collecting static files'
python manage.py collectstatic --no-input

echo '[INFO] Loading sensor fixture'
python manage.py loaddata sensors

exec "$@"
