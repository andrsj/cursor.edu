#include<conio.h>
#include<iostream>
#include<clocale>

using namespace std;

int a, b, u, v, n, i, j, ne = 1;
int visited[10] = { 0 },  mincost = 0, cost[10][10];
int mini = 0;
void main()
{
	setlocale(LC_ALL, "ru");

	int path[100] = { 0 }; //� ���� ������ ����� ������������ �������, �� ������� ����������� ����
	int path_index = 0;

	//clrscr();
	cout << "����1�� �1���1��� ������  "; cin >> n;
	cout << "����1�� ������� ������ ������ �� �� ��� \n";



	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
		{
			cin >> cost[i][j];

			if (cost[i][j] == 0)
				cost[i][j] = 999; //999 - ��� ���-���� �������������. ������ ���� ������ ��� �������� ���� ������� �� ����� � �����
		}
	visited[1] = 1;
	cout << "\n";

	while (ne < n)
	{
		for (i = 1, mini = 999; i <= n; i++)
			for (j = 1; j <= n; j++)
				if (cost[i][j]< mini)
					if (visited[i] != 0)
					{
						mini = cost[i][j];
						a = u = i;
						b = v = j;
					}
		if (visited[u] == 0 || visited[v] == 0)
		{
			path[path_index] = b;
			path_index++;
			//cout<<"\n "<<ne++<<"  "<<a<<"  "<<b<<min; //����� ������� ���
			ne++; //���� ������� ���� ����������������� - ��� ����������������
			mincost += mini;
			visited[b] = 1;

		}
		cost[a][b] = cost[b][a] = 999;
	}


	cout << "\n";

	cout << 1 << " --> ";
	for (int i = 0; i<n - 1; i++)
	{
		cout << path[i];
		if (i<n - 2) cout << " --> ";
	}

	cout << "\n ̳������� ���� �������  " << mincost;


	cin.get();
	cin.get();
	system("pause");
}