#include <iostream>
#include "Header.h"
#include <stdexcept>
#include <algorithm>
#include <conio.h>

using namespace std;

int n,k;
int A[100];

int Factorial(int n) 
{
	if (n == 0)
		return 1;
	else
		return n*(Factorial(n-1));
}

int C(int n, int k) 
{
	return Factorial(n) / (Factorial(k) * Factorial(n-k));
}

void GenPerm(int A[], int n)
{
	for (int i = n - 2; i >= 0; i--)
	{
		if (A[i] < A[i+1])
		{
			char min = A[i+1];
			char minPos = i+1;

			for (int j = i+1; j < n; j++)
			{
				if (min > A[j] && A[j] > A[i])
				{
					min = A[j];
					minPos = j;
				}
			}

			swap(A[i], A[minPos]);
			sort(A + i, A + n);
			break;
		}
	}
}

void swap (int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

void VuvidA (int A[], int n)
{
	for (int i=0; i < n; i++)
	{
		cout << A[i] << " ";
	}
	cout << endl;
}

void ZapovA (int A[], int n)
{
	for (int i = 0; i < n; i++)
	{
		cin >> A[i];
	}

	for (int h = 1; h < n; h++){
		for (int i = 0; i < n-1; i++ )
			if (A[i] > A[i+1])
		{
			int stk = A[i];
			A[i] = A[i+1];
			A[i+1] = stk;
		}
	}
}

void GenerC (int A[], int n, int k)
{
	for (int i = k - 1; i >= 0; i--)
	{
		if (A[i] != n - k + i + 1)
		{
			A[i] = A[i] + 1;

			for (int j = i + 1; j < k; j++)
			{
				A[j] = A[j - 1] + 1;
			}
			break;
		}
	}
}

int main()
{
      cout << "Vvedit n -> ";
      cin >> n;
      cout << "Vvedit k -> ";
      cin >> k;
	  cout << endl;
	  cout << "Vvedit elementu:" << endl;

	  if (k > n)
	  {
		  cout << "Eror" << endl;
		  system("pause");
	  }

	  ZapovA(A,n);

	  cout << endl;

      for (int i = 0; i < k; i++)
      {
        cout << A[i] <<" ";
      }

      cout<<endl;

      for (int i = 0; i < (C(n,k)) - 1; i++)
      {
        GenerC(A,n,k);
        VuvidA(A,k);
      }
 
	  system("pause");
	  return 0;
}