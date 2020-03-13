#pragma once
#include "stdafx.h"
#include <stdexcept>
#include "Comb.h"
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

namespace Combinatory {
		int part1 :: factorial(int n)
		{
			if (n == 0)
				return 1;
			else
				return n * factorial(n - 1);
		}

		int part1::A(int n, int k)
		{
			return part1::factorial(n) / factorial(n - k);
		}

		int part1::_A(int n, int k)
		{
			return pow(n, k);
		}

		int part1::C(int n, int k)
		{
			return part1::factorial(n) / (factorial(k) * factorial(n - k));
		}

		int part1::_C(int n, int k)
		{
			return part1::factorial(n + k - 1) / (factorial(k) * factorial(n - 1));


		}
		// ATTENTION! THERE THE SECOND PART BEGINS

		void swap(int *a, int i, int j)
		{
			int s = a[i];
			a[i] = a[j];
			a[j] = s;
		}

		bool part2::GenPerm(int *a, int n)
		{
			int j = n - 2;
			while (j != -1 && a[j] >= a[j + 1]) { j--; }
			if (j == -1)
				return false;
			int k = n - 1;
			while (a[j] >= a[k]) { k--; }
			swap(a, j, k);
			int l = j + 1, r = n - 1;
			while (l < r)
				swap(a, l++, r--);
			return true;
		}

		void print :: Print(int *a, int n)
		{
			static int num = 1;
			cout.width(6);
			cout << num++ << ": ";
			for (int i = 0; i < n; i++)
				cout << a[i] << " ";
			cout << endl;
		}

		//NWARNING! PART 3
		bool part3::GenComb(int *a, int n, int k)
		{
			for (int i = k - 1; i >= 0; i--)
				if (a[i] < n - k + i + 1)
				{
					++a[i];
					for (int j = i + 1; j < k; ++j)
						a[j] = a[j - 1] + 1;
					return true;
				}
			return false;
		}
	};