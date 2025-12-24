import pandas as pd

def converter(df):
    print("Converting dataframe to CSV...")
    df.to_csv(
        "data/output.csv",
        index=False,        
        sep=";",             
        encoding="utf-8-sig" # evita problema de acentuação no Excel
    )
    print("Conversion complete. File saved as data/output.csv")
if __name__ == "__main__":
    main()