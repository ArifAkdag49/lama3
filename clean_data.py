import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # Eksik değerleri kontrol etme ve doldurma
    df.fillna(method='ffill', inplace=True)
    
    # Veri tiplerini kontrol etme ve düzeltme
    df['HireDate'] = pd.to_datetime(df['HireDate'])
    
    return df

cleaned_df = clean_data('employees.csv')
cleaned_df.to_csv('cleaned_employees.csv', index=False)
