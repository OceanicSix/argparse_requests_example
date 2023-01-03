import argparse
parser=argparse.ArgumentParser(description=" A demo of how argparse works ")

parser.add_argument("firstname", help="Display the string you enter here", type=str) # define the argument

parser.add_argument("lastname", help="Display the string you enter here", type=str)

args=parser.parse_args()

print(args.firstname+args.lastname) #perform action to argument