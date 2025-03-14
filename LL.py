import psycopg2
import yaml
import pandas as pd

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def load_data():
    config = load_config()
    db_config = config['database']
    
    conn = psycopg2.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        dbname=db_config['dbname']
    )
    
    df = pd.read_csv('data/processed/processed_data.csv')
    
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO your_table (column1, column2, date)
                VALUES (%s, %s, %s)
            """, (row['column1'], row['column2'], row['date']))
        
        conn.commit()
    
    conn.close()

if __name__ == "__main__":
    load_data()
