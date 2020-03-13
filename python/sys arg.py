import sys
if len(sys.argv) != 2:		# 
	print("Enter plz arg")
	raise SystemExit(1)		#

f = open(sys.argv[1])
lines = f.readlines()
f.close()

fvalues = [float(line) for line in lines]
min(fvalues)
max(fvalues)