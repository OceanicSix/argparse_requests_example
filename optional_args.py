import argparse
parser=argparse.ArgumentParser(description=" A demo of how argparse works ")

parser.add_argument("user_str", help="Display the string you enter here",type=str)

parser.add_argument("-v","--verbose", help="More verbose output", action="count",default=0)

args=parser.parse_args()

if args.verbose >=2:
    print(f'Message type is {type(args.user_str)};\nMessage value is {args.user_str}')
elif args.verbose ==1:
    print(f'Message value is {args.user_str}')
else:
    print(args.user_str)
