import pandas as pd

def clean_data(items):
    df = pd.DataFrame(items)
    print(f"清洗前数据数量: {len(df)}")
    df.drop_duplicates(subset=['name'], inplace=True)
    df.dropna(subset=['name', 'price'], inplace=True)
    print(f"清洗后数据数量: {len(df)}")
    return df.to_dict(orient='records')