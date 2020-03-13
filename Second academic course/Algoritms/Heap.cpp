#include "stdafx.h"
#include <iostream>

using namespace std;
using namespace System;

int a[50], n, hs;

void MAX_HEAPIFY(int a[], int i, int n)
{
	int l, r, largest, loc;
	l = 2 * i;//le			ft
	r = (2 * i + 1);//right
	// якщо лівий нащадок більший за корінь
	if ((l <= n) && a[l] > a[i])
		largest = l;
	else
		largest = i;
	// якщо правий нащадок більший за найбільший корінь
	if ((r <= n) && (a[r] > a[largest]))
		largest = r;

	//якщо найбільший нащадок не є коренем
	if (largest != i)
	{
		loc = a[i];
		a[i] = a[largest];
		a[largest] = loc;
		MAX_HEAPIFY(a, largest, n);
	}
}

void BUILD_MAX_HEAP(int a[], int n)
{  //будується купа
	for (int k = n / 2; k >= 1; k--)
	{  
		MAX_HEAPIFY(a, k, n);
	}
}

//головна функція сортування
void HEAPSORT(int a[], int n)
{

	BUILD_MAX_HEAP(a, n);
	int i, temp;
	for (i = n; i >= 2; i--)
	{
		temp = a[i];
		a[i] = a[1];
		a[1] = temp;
		//викликається имаксимальше з зменшеної купи
		MAX_HEAPIFY(a, 1, i - 1);
	}
}

int main()
{
	int n;
	int i;

	cout << "Enter the size of the array: " ;
	cin >> n;
	
	cout << "Enter the elements in the array: " ;
	for (int i = 1; i <= n; i++)
	{
		cin >> a[i];
	}
	HEAPSORT(a, n);
	
	cout << endl << "Sorted elements: \n";
	for (int i = 1; i <= n; i++)
	{
		cout << a[i] ;
		if (i != n)
		{
			cout << " ";
		}
	}
	cout << " " << endl;
	system("pause");
}