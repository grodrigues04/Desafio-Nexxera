from src import constants
from datetime import datetime

def position_comma(value):
    value = str(value)
    value = value.replace(",", "")
    comma_position = len(value) - 2  # define first comma position
    while comma_position > 0:
        value = value[:comma_position] + "," + value[comma_position:]
        comma_position -= 3  # jump three positions back
    return value

def timestamp_to_string(ts: datetime) -> str:
    return f"{ts.day:02d}/{constants.MONTHS_MAP[ts.month]}/{ts.year}"


def formater(rule, data, column=None, extraRule=None):

    match rule:
        case constants.POINTS_LINES:
            new_column = []
            for value in data:
                new_column.append(value.replace("/", "").replace(".", "").replace("-", ""))
            return new_column

        case constants.STATES:
            return [constants.BRAZILIAN_STATES_MAP[value] for value in data]

        case constants.DATE:
            return [timestamp_to_string(value) for value in data]

        case constants.PAYMENT_AMOUNT:
            return [position_comma(value) for value in data]


if __name__ == "__main__":
    formater()