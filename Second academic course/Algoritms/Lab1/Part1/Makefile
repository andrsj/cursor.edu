CC = g++

all: Main.exe

Main.exe: Main.o Graph.o
	$(CC) Main.o Graph.o -o $@

Main.o: Main.cpp
	$(CC) -c $^ -o $@

Graph.o: Graph.cpp
	$(CC) -c $^ -o $@

clear:
	rm -rf *.o *.exe	
