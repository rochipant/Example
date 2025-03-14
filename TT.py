import pandas as pd

def transform_data(raw_data):
    # Convertir a DataFrame
    df = pd.DataFrame(raw_data)
    
    # Ejemplo de transformación: filtrar y limpiar datos
    df = df[df['value'] > 0]  # Filtrar valores positivos
    df['date'] = pd.to_datetime(df['date'])  # Convertir columna a datetime
    
    return df

if __name__ == "__main__":
    import json
    with open('data/raw/raw_data.json', 'r') as file:
        raw_data = json.load(file)
    
    transformed_data = transform_data(raw_data)
    transformed_data.to_csv('data/processed/processed_data.csv', index=False)
