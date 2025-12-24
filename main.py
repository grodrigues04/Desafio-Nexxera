import pandas as pd
import os
from dotenv import load_dotenv
import src.constants as constants
from src.formater import formater
from src.converter import converter

def main():
    load_dotenv()

    columns_rules = os.getenv("COLUMNS_TO_FORMART", "").split(",")
    df = pd.read_excel('data/arquivo_entrada.xlsx')

    for column_name in df.columns:
        column_formart = column_name.upper().replace(" ", "_")
        if column_name in columns_rules:
            column_formart = column_name.upper().replace(" ", "_")
            print("Formarting column:", column_name)
            rule = constants.COLUMN_FORMAT_RULES.get(column_formart)
            df[column_name] = formater(rule, df[column_name])

    if os.getenv("COLUMN_ORDER"):
        print("Ordering by column:", os.getenv("COLUMN_ORDER"))
        typeOrder = os.getenv("ASCENDING", "False").lower() == "true"
        df_order = df.sort_values(by=os.getenv("COLUMN_ORDER"), ascending=typeOrder)
        converter(df_order)
    else:
        converter(df)
if __name__ == "__main__":
    main()