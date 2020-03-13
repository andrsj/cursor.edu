// LogOn.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include "Comb2.h"
#include <stdexcept>
#include <iostream>
#include <algorithm>

using namespace std;

namespace Math {

	int Comb::Factorial(int n) {
			if (n == 0)
				return 1;
			else
				return n*(Comb::Factorial(n-1));
	}
	
	void Comb::GenPerm(int* A, int n) {
		for (int i = 1; i = n; i++) {
			if (A[n - (1 + n)] < A[n - i]) {
				sort(A+(n - i + 1), A+n);
				Comb::swap(A,n - (i + 1),n - 1);
				break;
			}
		}
	}

	void Comb::swap(int *a, int i, int j) {
		int s = a[i];
		a[i] = a[j];
		a[j] = s;
	}
}