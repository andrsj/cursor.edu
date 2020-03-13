// Comb.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include <iostream>
#include "Comb.h"
#include <stdexcept>

using namespace std;

namespace Math {

	int MyComb::Factorial(int n)
	{
		if (n==0)
			return 1;
		else
			return n*Factorial(n-1);
	}
	
	void swap (int *a,int i, int j)
	{
		int s = a[i];
		a[i] = a[j];
		a[j] = s;
	}
	bool MyComb::GenPerm(int *a, int n)
	{
		int j = n - 2;
		while (j != -1 && a[j] >= a[j+1]) {j--;}
		if (j ==-1)
			return false;
		int k = n-1;
		while (a[j] >= a[k]) {k--;}
		swap(a, j, k);
		int l = j + 1, r = n - 1;
		while (l < r)
			swap (a, l++, r--);
		return true;
	}

	void MyComb::Print(int *a, int n)
	{
		static int num = 1;
		cout.width(6);
		cout << num++ << ": ";
		for (int i = 0; i < n; i++) 
			cout << a[i] << " ";
		cout <<endl;
	}

	bool MyComb::GenComb(int *a, int n, int k)
	{
		for (int i = k-1; i >= 0; i--)
			if(a[i] < n-k+i+1)
			{
				++a[i];
				for (int j = i+1; j<k; ++j)
					a[j] = a[j-1]+1;
				return true;
			}
			return false;
	}
}