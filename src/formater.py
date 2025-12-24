from src import constants
from datetime import datetime

def formater(type_data, data, column=None, extraRule=None):

    match type_data:
    
        case constants.POINTS_LINES:
            new_column = []
            for value in data:
                new_column.append(value.replace("/", "").replace(".", "").replace("-", ""))
            return new_column




if __name__ == "__main__":
    formater()