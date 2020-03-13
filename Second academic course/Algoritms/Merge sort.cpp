﻿
#include "stdafx.h"
#include <iostream>
using namespace std;
using namespace System;

int a[50];
void merge(int, int, int);
void merge_sort(int low, int high)
{
	int mid;
	if (low < high) 
	{
		mid = (low + high) / 2; //знаходимо середину послідовності
		merge_sort(low, mid);
		merge_sort(mid + 1, high);
		merge(low, mid, high);
	}
}
void merge(int low, int mid, int high)
{
	int h, i, j, b[50], k;
	h = low;//індекс першого шляху
	i = low;//індекс другого шляху
	j = mid + 1;//індекс елементу результуйочої послідовності

	while ((h <= mid) && (j <= high))
	{
		//покт не дійшли до кінця шляху, заповнюємо
		//елемент шляху який формулюється меншим значенням з 2х
		if (a[h] <= a[j])
		{
			b[i] = a[h];
			h++;
		}
		else
		{
			b[i] = a[j];
			j++;
		}
		i++;
	}
	//переписуємо елементи які залишились з другого шляху
	if (h > mid)
	{
		for (k = j;k <= high;k++)
		{
			b[i] = a[k];
			i++;
		}
	}
	else
	{
		for (k = h;k <= mid;k++)
		{
			b[i] = a[k];
			i++;
		}
	}
	for (k = low;k <= high;k++) a[k] = b[k];
}
void main()
{
	int num, i;

	cout << "Please Enter THE NUMBER OF ELEMENTS you want to sort: ";
		cin >> num;
	cout << endl;
	cout << "Please Enter  " << num << "  ELEMENTS: ";
		for (i = 1;i <= num;i++)
		{
			cin >> a[i];
		}
	merge_sort(1, num);
	cout << endl;
	cout << " MERGE SORT RESULT:" ;
	cout << endl ;

	for (i = 1;i <= num;i++)
		cout << a[i] << "	";

	cout << endl << endl << endl << endl;
	

}
