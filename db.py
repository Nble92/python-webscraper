import psycopg2
import yaml


def load_config(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)

config = load_config('config.yaml')

db_config = config['database']

print(db_config)

# Establish a connection
conn = psycopg2.connect(
    dbname=db_config['name'], 
    user=db_config['user'], 
    password=db_config['password'], 
    host=db_config['host'], 
    port=db_config['port']
)
def get_db_connection():
    return conn

def close_connection():
    return conn.close()

# Create a cursor object
cursor = conn.cursor()
