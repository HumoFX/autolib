# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
#echo "Apply database migrations"
#python manage.py makemigrations
#python manage.py migrate
# Start server
echo "Starting server"
#python manage.py runserver 0.0.0.0:8000
PROCESSOR_COUNT=$(nproc)
GUNICORN_WORKER_COUNT=$(( PROCESSOR_COUNT * 2 + 1 ))
gunicorn -w ${GUNICORN_WORKER_COUNT} -b 0.0.0.0:8000 elib.wsgi --timeout 600 --reload


#gunicorn -b 0.0.0.0 -p 8000 wsgi.asgi:application