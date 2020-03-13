#include <iostream>
#include <cmath>
#include "Header.h"

using namespace std;

long double fact(int N){

	if(N < 0) 
        return 0; 
    if (N == 0) 
        return 1; 
    else 
        return N * fact(N - 1);
}

int A(int N, int K){

	return fact(N)/fact(N-K);
}

int _A (int N, int K){

	return pow(N,K);
}

int C (int N, int K){
	
	return fact(N)/(fact(K)*fact(N-K));
}

int _C (int N, int K){

	return fact(N+K-1)/(fact(K)*fact(N-1));
}


int main()
{
	int N,K;
    cout << "Vvedit N: ";
    cin >> N;
	cout << "Vvedit K: ";
	cin >> K;

	if (N<K){
		cout << "Pomulka - K > N\n";
		system ("pause");
		return 0;
	} else
	{
    cout << "n! = " << fact(N) << endl;
	cout << "A = " << A(N,K) << endl;
	cout << "_A = " << _A(N,K) << endl;
	cout << "C = " << C(N,K) << endl;
	cout << "_C = " << _C(N,K) << endl;

	system ("pause");
	}

    return 0;
}