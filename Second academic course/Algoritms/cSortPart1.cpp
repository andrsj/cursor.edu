// ConsoleApplication1.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <time.h>
 

using namespace std;
 const int MAX = 10;
 	
class cSort
{
public:
    void sort( int* arr, int len )
    {
	int mi, mx, z = 0; findMinMax( arr, len, mi, mx );
	int nlen = ( mx - mi ) + 1; int* temp = new int[nlen];
	memset( temp, 0, nlen * sizeof( int ) );
 
	for( int i = 0; i < len; i++ ) temp[arr[i] - mi]++;
 
	for( int i = mi; i <= mx; i++ )
	{
	    while( temp[i - mi] )
	    {
		arr[z++] = i;
		temp[i - mi]--;
	    }
	}
 
	delete [] temp;
    }
 
private:
    void findMinMax( int* arr, int len, int& mi, int& mx )  //знаходження максимального і мінімального елементу
    {
	mi = INT_MAX; mx = 0;
	for( int i = 0; i < len; i++ )
	{
	    if( arr[i] > mx ) mx = arr[i];
	    if( arr[i] < mi ) mi = arr[i];
	}
    }
};

int main( int argc, char* argv[] )
{     setlocale(LC_ALL,"Rus");
      cout<<"**********************"<<endl;
      cout<<"Сортування пiдрахунком"<<endl;
      cout<<"**********************"<<endl;

    srand( time( NULL ) ); int arr[MAX];
    for( int i = 0; i < MAX; i++ )
	arr[i] = rand() % 50 - rand() % 10;
    cout<<"Вхiдний масив: "<<endl;
    for( int i = 0; i < MAX; i++ )
	cout << arr[i] << ", ";
    cout << endl << endl;
 
    cSort s; s.sort( arr, MAX );
    cout<<"\nРезультуючий масив: "<<endl;
    for( int i = 0; i < MAX; i++ )
	cout << arr[i] << ", ";
    cout << endl << endl;
 
  system("pause>>void");;
}

