# foo.py
import optparse
p = optparse.OptionParser()

# Simple argv
p.add_option("-t", action="store_true", dest="tracing")

# String
p.add_option("-o", "--outfile", action="store", type="string", dest="outfile")

# Int
p.add_option("-d", "--debuglevel", action="store", type="int", dest="debug")

# Параметр із запропонованих в choices
p.add_option("--speed", action="store", type="choice", dest="speed",
choices=["slow","fast","ludicrous"])

# Параметр, що приймає декілька аргументів (к-сть -> nargf)
p.add_option("--coord", action="store", type="int", dest="coord", nargs=2)

# Група параметрів, значення яких зберігається в одному атрибуті
p.add_option("--novice", action="store_const", const="novice", dest="mode")
p.add_option("--guru", action="store_const", const="guru", dest="mode")

# За умовчанням
p.set_defaults(tracing=False,
debug=0,
speed="fast",
coord=(0,0),
mode="novice")

# Проаналізувати аргументи
opt, args = p.parse_args()

# Вивести значення аргументів
print("tracing :", opt.tracing)
print("outfile :", opt.outfile)
print("debug :", opt.debug)
print("speed :", opt.speed)
print("coord :", opt.coord)
print("mode :", opt.mode)

# Вивести аргументи, що залишилися
print("args :", args)





"""
% python foo.py -h
usage: foo.py [options]

options:
-h, --help show this help message and exit
-t
-o OUTFILE, --outfile=OUTFILE
-d DEBUG, --debuglevel=DEBUG
--speed=SPEED
--coord=COORD
--novice
--guru



% python foo.py -t -o outfile.dat -d 3 --coord 3 4 --speed=ludicrous blah
tracing : True
outfile : outfile.dat
debug : 3
speed : ludicrous
coord : (3, 4)
mode : novice
args : [‘blah’]

% python foo.py --speed=insane
usage: foo.py [options]

foo.py:error:option --speed:invalid choice:’insane’
(choose from ‘slow’, ‘fast’, ‘ludicrous’)
"""