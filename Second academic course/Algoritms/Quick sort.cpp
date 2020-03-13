#include <iostream>

using namespace std;

void quick_sort(int[], int, int);
int partition(int[], int, int);

int main()
{
	int a[50], n, i;
	cout << "           QUICK SORING ";
	cout << "\nHow many elements do you want to sort? ";
	cin >> n;
	cout << "\n Enter the array elements: ";
	for (i = 0;i < n;i++){
		cout << "\nEnter element " << i + 1 << ": ";
		cin >> a[i];
}
	quick_sort(a, 0, n - 1);
	cout << "\n Array after sorting: ";
	for (i = 0;i < n;i++)
		cout << a[i] << " ";
	cout << "\n";
	system("pause");
	return 0;
	
}

void quick_sort(int a[], int l, int u)
{
	int j;
	if (l < u)
	{
		j = partition(a, l, u);
		quick_sort(a, l, j - 1);
		quick_sort(a, j + 1, u);
	}
}

int partition(int a[], int l, int u)
{//дана функція повертає індекс з опорним елементом, що роз масив на 2 частини
	int v, i, j, temp;
	v = a[l];//вибираємо опорний елемент
	i = l;  
	j = u + 1;
	// 2 масиви
	// менші за опорний розміщуються зліва, а більші справа
	do
	{
		do
			i++;

		while (a[i] < v&&i <= u);

		do
			j--;
		while (v < a[j]);

		if (i < j)
		{
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		}
	} while (i < j);

	a[l] = a[j];
	a[j] = v;

	return(j);
}
