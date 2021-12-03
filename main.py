"""
WRITTEN BY: Siyabend Ürün
"""
import argparse
import exrex
import sys

DEFAULT_RANGE = 50
DEFAULT_FILE_COUNT = 10
INPUT_DIRECTORY = "./Inputs/"
INPUT_FILE = INPUT_DIRECTORY + 'inputs'

REG_PLATE_EXP = r'[0-7]\d [A-Z]{2} \d{4}'
CAR_TYPE_EXP = r'[1-6]'
WEIGHT_EXP = r'\d\d\d\d'
NAME_EXP = r'[A-Z][a-z]{3,5} [A-Z][a-z]{3,5}'
TIME_EXP = r'\d\d\d\d'
SPECIAL_CASE_EXP = r'[yge]'

parser = argparse.ArgumentParser()
parser.add_argument('get_range', nargs="?", default=DEFAULT_RANGE, type=int)
parser.add_argument('file_count', nargs="?", default=DEFAULT_FILE_COUNT, type=int)
args = parser.parse_args()


expressions = {
    'reg_plate': REG_PLATE_EXP,
    'car_type': CAR_TYPE_EXP,
    'weight': WEIGHT_EXP,
    'time_exp': TIME_EXP,
    'name': NAME_EXP,
}

def create_sample():
    values = [exrex.getone(exp) for exp in expressions.values()]
    values[1] in ['1', '2'] and values.append(exrex.getone(SPECIAL_CASE_EXP))
    return values


def create_inputs(count):
    for i in range(count):
        for text in create_sample():
            print(text)
        if i != count - 1:
            print("e")
    print("h")


def main():
    for i in range(args.file_count):
        with open(f'{INPUT_FILE}{i}.txt', 'w') as file:
            sys.stdout = file
            create_inputs(args.get_range)


main()