from decouple import config
import traceback
import psycopg2
params = {
    'dbname': config('DB_NAME', default='book_db'),
    'user': config('DB_USER', default='postgres'),
    'password': config('DB_PASSWORD', default='postgres'),
    'host': config('DB_HOST', default='127.0.0.1'),
    'port': config('DB_PORT', default='5432'),
    'options': '-c client_encoding=WIN1251',
}
print('Params:', params)
try:
    conn = psycopg2.connect(**params)
except Exception as e:
    traceback.print_exc()
    print('Exception repr:', repr(e))
