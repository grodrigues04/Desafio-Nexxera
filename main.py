import argparse
import sys
import pandas as pd
import os
import src.constants as constants
from src.formater import formater
from src.converter import converter

COLUMN_ORDER = "Forma Lancamento"
COLUMNS_TO_FORMART = ["Numero Incricao Empresa", "Estado", "Data Pagamento", "Valor Pagamento"]


def main():

    parser = argparse.ArgumentParser(description="Script que recebe dois paths de arquivos")
    parser.add_argument("input_file_path", help="Path do primeiro arquivo")
    parser.add_argument(
        "output_file_path",
        nargs="?",           #Makes it optional
        default="output",    #Default value
        help="Nome do arquivo de saída (sem extensão)"
    )

    args = parser.parse_args()

    input_file_path = args.input_file_path 
    output_file_path = args.output_file_path

    if not os.path.isfile(input_file_path):
        print(f"Error: file not found: {input_file_path}")
        sys.exit(1)

    #Cases of invalid or corrupted files
    try:
        df = pd.read_excel(input_file_path)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        sys.exit(1)

    for column_name in df.columns:
        if column_name in COLUMNS_TO_FORMART:
            column_formart = column_name.upper().replace(" ", "_")
            print("Formarting column:", column_name)
            rule = constants.COLUMN_FORMAT_RULES.get(column_formart)
            df[column_name] = formater(rule, df[column_name])


    print(f"Ordering by column: {COLUMN_ORDER}")
    df_order = df.sort_values(by=COLUMN_ORDER, ascending=True)
    converter(df_order, output_file_path)

if __name__ == "__main__":
    main()