import psycopg2

from environs import Env

env = Env()
env.read_env(override=True)
try:
    conn = psycopg2.connect(
    host=env('host'),
    user=env('user'),
    password=env('password'),
    port=env('port'),
    dbname=env('dbname')
    )
except Exception as e:
    print(e)


data_base = {}