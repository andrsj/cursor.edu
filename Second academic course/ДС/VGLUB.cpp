#include <iostream>

using namespace std;

const int n = 7;
int i, j;
bool *visited = new bool[n];

//матриця
int graph[n][n] =
{
{0, 1, 1, 0, 0, 0, 0},
{1, 0, 1, 0, 0, 0, 0},
{1, 1, 0, 1, 0, 0, 1},
{0, 0, 1, 0, 1, 0, 0},
{0, 0, 0, 1, 1, 0, 1},
{0, 0, 0, 0, 1, 0, 1},
{0, 0, 1, 0, 1, 1, 0}
};

//пошук вглиб
void DFS (int st){
	int r;
	cout << st + 1 << " ";
	visited[st] = true;
	for (r = 0; r <= n; r++)
		if ((graph[st][r] != 0) && (!visited[r]))
			DFS(r);
}


void main(){
	setlocale(LC_ALL, "Rus");
	int start;
	cout << "Матриця: " << endl;
	for (i=0; i<n; i++){
		visited[i] = false;
		for (j = 0; j < n; j++)
			cout << " " << graph[i][j];
		cout << endl;
	}

	cout << "Стартова вершина >> "; 
	cin >> start;

	//start = 1;
	
	//масив відвіданих вершин
	bool *vis=new bool[n];
	cout << "Порядок обходу -> ";
	DFS(start-1);
	delete []visited;
	cout << endl;
	
	system("pause");
}