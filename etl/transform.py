import pandas as pd

def transform_data(df):
    column_map = {
        "mfr": "manufacturer",
        "type": "type",
        "potass": "potassium"
    }
    df.rename(columns=column_map, inplace=True)

    mfr_map = {
        'A': 'American Home Foods',
        'G': 'General Mills',
        'K': 'Kelloggs',
        'N': 'Nabisco',
        'P': 'Post',
        'Q': 'Quaker Oats',
        'R': 'Ralston Purina'
    }
    type_map = {'C': 'cold', 'H': 'hot'}

    df['manufacturer'] = df['manufacturer'].map(mfr_map)
    df['type'] = df['type'].map(type_map)

    # Filter out rows with 0 or missing calories/protein
    df = df[(df['calories'] > 0) & (df['protein'] > 0)]

    # Normalize strings to lowercase
    string_cols = df.select_dtypes(include='object').columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.lower()

    # Example transformation: replicate values with scaling (e.g., for demonstration)
    nutrition_cols = ['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potassium']
    for col in nutrition_cols:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: f"{x}, {x * 12}" if pd.notnull(x) else x)

    return df
