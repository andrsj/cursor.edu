//  Prim's Minimum 

#include <stdio.h> 
#include <limits.h> 
#include <stdbool.h> 
#include <iostream>
using namespace std;

#define V 9

int Bagato = 10e+10;

int minKey(int key[], bool mstSet[])
{
	int min = Bagato, min_index;

	for (int v = 0; v < V; v++)
		if (mstSet[v] == false && key[v] < min)
			min = key[v], min_index = v;

	return min_index;
}

void printMST(int parent[], int n, int graph[V][V])
{
	int k = 1;
	for (int i = 1; i < V; i++) {
		cout << "\tEdge = [V" << parent[i] << "; V" << i << "] cost = " << graph[i][parent[i]] << "." << endl;
		k += i;
	}
	cout << "\n\tMin Weight = " << k << "." << endl;
}


void primMST(int graph[V][V])
{
	int parent[V];
	int key[V];
	bool mstSet[V];

	for (int i = 0; i < V; i++)
		key[i] = Bagato, mstSet[i] = false;
	
	key[0] = 0;
	parent[0] = -1; 
	
	for (int count = 0; count < V - 1; count++)
	{
		int u = minKey(key, mstSet);
		mstSet[u] = true;

		for (int v = 0; v < V; v++)		
			if (graph[u][v] && mstSet[v] == false && graph[u][v] < key[v])
				parent[v] = u, key[v] = graph[u][v];		
	}

	printMST(parent, V, graph);                                                                                                                                                                                                   	
}


int main()
{
	int graph[V][V] = { {Bagato, 4, Bagato, Bagato, Bagato, Bagato, Bagato, 8, Bagato},
						{4, Bagato, 8, Bagato, Bagato, Bagato, Bagato, 11, Bagato},
						{Bagato, 8, Bagato, 7, Bagato, 4, Bagato, Bagato, 2},
						{Bagato, Bagato, 7, Bagato, 9, 14, Bagato, Bagato, Bagato},
						{Bagato, Bagato, Bagato, 9, Bagato, 10, Bagato, Bagato, Bagato},
						{Bagato, Bagato, 4, 14, 10, Bagato, 2, Bagato, Bagato},
						{Bagato, Bagato, Bagato, Bagato, Bagato, 2, Bagato, 1, 6},
						{8, 11, Bagato, Bagato, Bagato, Bagato, 1, Bagato, 7},
						{Bagato, Bagato, 2, Bagato, Bagato, Bagato, 6, 7, Bagato} };

	cout << "\n\t       Prima Algoritms" << endl;
	cout << "\n\t         -- Weight --\n" << endl;

	primMST(graph);

	cout << endl;
	system("pause");
	return 0;
}
