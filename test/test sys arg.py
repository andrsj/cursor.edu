import sys
if len(sys.argv) != 3:
    sys.stderr.write("Usage: python '%s' inputfile outputfile\n" % sys.argv[0])
    raise SystemExit(1)
inputfile = sys.argv[1]
outputfile = sys.argv[2]
print(inputfile,outputfile)