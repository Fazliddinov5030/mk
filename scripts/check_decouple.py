from decouple import config
keys = ['DB_NAME','DB_USER','DB_PASSWORD','DB_HOST','DB_PORT','SECRET_KEY']
for k in keys:
    try:
        v = config(k)
    except Exception as e:
        v = f'<error: {e!r}>'
    print(f"{k} -> {repr(v)}")
