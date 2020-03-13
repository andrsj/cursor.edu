CC = g++

all: Main.exe

Main.exe: Main.o Tree.o
	$(CC) Main.o Tree.o -o $@

Main.o: Main.cpp
	$(CC) -c $^ -o $@

Tree.o: Tree.cpp
	$(CC) -c $^ -o $@

clear:
	rm -rf *.o *.exe
