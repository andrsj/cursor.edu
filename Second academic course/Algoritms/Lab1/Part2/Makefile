CC = g++

all: Main.exe

Main.exe: Main.o
	$(CC) Main.o -o $@

Main.o: Main.cpp
	$(CC) -c $^ -o $@

clear:
	rm -rf *.o *.exe	
