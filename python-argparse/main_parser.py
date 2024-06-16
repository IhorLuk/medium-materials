import argparse
import random

parser = argparse.ArgumentParser(
    prog="main_parser.py",
    description="How to use argparse library?"
)
#parser.add_argument("first_name", help="Provide first name to greet you.")
parser.add_argument("--numbers",
                    help="make two guesses for numbers between 1 and 10",
                    type=int,
                    choices=list(range(1, 11)),
                    required=True,
                    nargs=2
                    )

parser.add_argument("--process",
                    help="make any guesses",
                    action="store_true")
args = parser.parse_args()
random_int = random.randint(0, 10)

print(args.process)
if args.process:
    for number in args.numbers:
        if random_int == number:
            print("Correct! Number is: ", random_int)
            exit(1)
            
    print("Number was: ", random_int)


#print(f"Hello, {args.first_name}!")