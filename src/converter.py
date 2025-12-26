import pandas as pd

def converter(df, output_name="output"):
    print("Converting dataframe to CSV...")
    output_path = f"data/{output_name}.csv"
    df.to_csv(
        output_path,
        index=False,        
        sep=";",             
        encoding="utf-8-sig" # evita problema de acentuação no Excel
    )
    print(f"Conversion complete. File saved as {output_path}")
if __name__ == "__main__":
    converter()