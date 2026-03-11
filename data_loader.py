import pandas as pd

def get_clean_data(file_path):
    # Load data
    df = pd.read_csv(file_path, sep=';', encoding='utf-8-sig', low_memory=False)
    
    # 1. Buang Nan di kolom 'make'
    df = df.dropna(subset=['make'])
    
    # 2. Gabungkan Vw ke Volkswagen
    df['make'] = df['make'].replace('Vw', 'Volkswagen')
    
    # 3. List brand sesuai permintaanmu
    allowed_brands = [
        'Acura','Bmw','Cadillac','Chevrolet','Chrysler','Dodge','Ford','Gmc',
        'Honda','Hyundai','Infiniti','Jeep','Kia','Land Rover','Lexus','Lincoln',
        'Mazda','Mercedes-Benz','Mercury','Mini','Mitsubishi','Nissan','Oldsmobile',
        'Pontiac','Porsche','Ram','Saturn','Subaru','Suzuki','Toyota','Volkswagen','Volvo'
    ]
    
    # Filter brand
    df = df[df['make'].isin(allowed_brands)]
    
    return df