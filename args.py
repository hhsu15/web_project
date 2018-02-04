import sys

def double(x):
	return x*2
argv = sys.argv
if len(argv) == 2:
	arg = int(argv[1])
	print(double(arg))