# -_*_coding=utf-8_*_

##############################
# Diceware PWD Generator     #
##############################
# Version: 1.0.0
# Author: Shokone


from wordlist import wordlist
import secrets
import sys
import argparse

NAME = "Diceware Pwd Generator"
VERSION = "1.0.0"

def banner():
	banner = '''
 ____  ____  ____  _      ____  _____ _____ _     
/  _ \\/   _\\/  __\\/ \\  /|/  _ \\/  __//  __// \\  /|
| | \\||  /  |  \\/|| |  ||| | \\|| |  _|  \\  | |\\ ||
| |_/||  \\__|  __/| |/\\||| |_/|| |_//|  /_ | | \\||
\\____/\\____/\\_/   \\_/  \\|\\____/\\____\\\\____\\\\_/  \\|
                                                  
	(Diceware PWD Generator by Shokone)
	'''

	return print(banner)

# create arguments passed by cmd
def cmdArguments(argv=None):
	# check if argv isn't empty
	if not argv:
		argv = sys.argv

	parse = argparse.ArgumentParser()

	# options available
	parse.add_argument("-v", "--version", dest="version", action="store_true", help="Show version number and exit.")
	parse.add_argument("-n", "--number", dest="num", help="Specify the number of words use to generate password")

	# check if arguments are correct
	for i in range(len(argv)):
		if any(arg in argv for arg in ("-v", "--version")):
			print("%s Version: %s" %(NAME,VERSION))
			raise SystemExit

		elif not any(arg in argv for arg in ("-n", "--number")) and "-h" not in argv:
			errormsg = "Missing a mandatory option (-n, --number). Use -h for show help"
			parse.error(errormsg)

	try:
		if hasattr(parse, "parse_known_args"):
			(args, arg) = parse.parse_known_args(argv)
		else: 
			parse.parse_args(argv)
	except SystemExit:
		raise SystemExit(0)

	return args


def start(args):
	COUNT = 5
	rolls = []
	wlist = []

	try:
		num = int(args.num)
		if num <= 0:
			print("\n[ERROR] Sorry, Number can't be negative or zero\n")
			raise SystemExit
	except ValueError:
		print("\n[ERROR] Sorry, Input must be a number.\n")
		raise SystemExit

	for _ in range(num):
		dice = ''.join(str(secrets.randbelow(6) + 1) for _ in range(COUNT)) 
		rolls.append(dice)

	for i in rolls:
		for j, k in wordlist.items():
			if i == j:
				wlist.append(k)

	print('\n[INFO] Your words are ')
	for i in wlist:
		print(i, end=' ')

	passphrase = " ".join(wlist).replace(" ", "")	

	print('\n\n[INFO] Your passphrase is ')
	print(passphrase)


# main function
def main():
	# print banner
	banner()

	# check arguments
	args = cmdArguments()
	start(args)

	

if __name__ == "__main__":
	try:
		main()
	except SystemExit as e:
		pass 


