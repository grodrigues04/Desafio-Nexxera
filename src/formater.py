from src import constants
from datetime import datetime

def formater(type_data, data, column=None, extraRule=None):

    match type_data:
    
        case constants.POINTS_LINES:
            new_column = []
            for value in data:
                new_column.append(value.replace("/", "").replace(".", "").replace("-", ""))
            return new_column

        case constants.STATES:
            new_column = []
            for value in data:
                new_column.append(constants.brazilian_states[value])
            return new_column

        case constants.DATE:
            new_column = []
            for value in data:
                day = value.day
                month_name = constants.mouths[value.month]
                year = value.year
                year = int(f"{year:02d}")
                new_column.append(f"{day:02d}/{month_name}/{year}")
            return new_column

        case constants.PAYMENT_AMOUNT:
            new_column = []
            for value in data:
                value = str(value)
                if "," not in value:
                    value = f"{value},00"
                value = f"R${value}"
                new_column.append(value)        
            return new_column


if __name__ == "__main__":
    formater()