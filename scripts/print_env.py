import os
keys=['DB_NAME','DB_USER','DB_PASSWORD','DB_HOST','DB_PORT','SECRET_KEY']
for k in keys:
    v=os.environ.get(k)
    print(f"{k} -> {repr(v)}")
