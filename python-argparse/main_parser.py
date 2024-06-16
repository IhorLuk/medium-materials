import argparse

parser = argparse.ArgumentParser(
    prog="main_parser.py",
    description="How to use argparse library?"
)
parser.add_argument("first_name", help="Provide first name to greet you.")
args = parser.parse_args()

print(f"Hello, {args.first_name}!")