#include <iostream> 
using namespace std;

#define V 9 
int parent[V];

int Bagato = 10 * 10;

int set_find(int i)
{
	while (parent[i] != i)
		i = parent[i];
	return i;
}

void union1(int i, int j)
{
	int a = set_find(i);
	int b = set_find(j);
	parent[a] = b;
}

void kruskalMST(int cost[][V])
{
	int mincost = 0; 

	for (int i = 0; i < V; i++)
		parent[i] = i;

	int edge_count = 0;
	while (edge_count < V -1) {
		int min = Bagato, a = -1, b = -1;
		for (int i = 0; i < V; i++) {
			for (int j = 0; j < V; j++) {
				if (set_find(i) != set_find(j) && cost[i][j] < min) {
					min = cost[i][j];
					a = i;
					b = j;
				}
			}
		}

		union1(a, b);

		cout << "\tEdge = [V" << a << "; V" << b << "] cost = " << min << endl;

		mincost += min;
		edge_count++;
	}

	cout << "\n\tMin Weight = " << mincost << ".\n" << endl;
}


int main()
{
	int cost[][V] = {   {Bagato, 4, Bagato, Bagato, Bagato, Bagato, Bagato, 8, Bagato},
						{4,	Bagato, 8, Bagato, Bagato, Bagato, Bagato, 11, Bagato},
						{Bagato, 8, Bagato, 7, Bagato, 4, Bagato, Bagato, 2},
						{Bagato, Bagato, 7, Bagato, 9, 14, Bagato, Bagato, Bagato},
						{Bagato, Bagato, Bagato, 9, Bagato, 10, Bagato, Bagato, Bagato},
						{Bagato, Bagato, 4, 14, 10, Bagato, 2, Bagato, Bagato},
						{Bagato, Bagato, Bagato, Bagato, Bagato, 2, Bagato, 1, 6},
						{8, 11, Bagato, Bagato, Bagato, Bagato, 1, Bagato, 7},
						{Bagato, Bagato, 2, Bagato, Bagato, Bagato, 6, 7, Bagato} };

	cout << "\n\t   Kruskal Algorithms" << endl;
	cout << "\n\t     -- Weight --\n" << endl;

	kruskalMST(cost);

	system("pause");
	return 0;
	

}
