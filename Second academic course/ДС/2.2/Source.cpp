#include <iostream>
#include <vector>
#include<algorithm>
 
using namespace std;

int n;
int a[100];

int step1()
{
    int j = INT_MAX;
    for (int i = 0; i < n - 1; i++)
    {
        if (a[i] < a[i + 1])
            j = i;
    }
    return j;
}
 
void step2(int i)
{
    int j_max;
	for (int j = i + 1; j < n; j++)
    {
        if (a[i] < a[j])
            j_max = j;
    }
    swap(a[i], a[j_max]);
}
 
int main()
{
	int i;

	cout << "Vvedit kilkist elementiv -> ";
	cin >> n;

	cout << "Vvedit elementu" << endl;
	for (i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	cout << endl;
	
	//сортує масив по зростанню
	for (int h = 1; h < n; h++){
		for (i = 0; i < n-1; i++ )
			if (a[i] > a[i+1])
		{
			int stk = a[i];
			a[i] = a[i+1];
			a[i+1] = stk;
		}
	}

	for (int i=0;i<n;i++)
		{
			cout << a[i]<<" ";
		}
		cout<<endl;

    int i_max;
    while ((i_max = step1()) != INT_MAX)
	{
        step2(i_max);
        // step 3
		for (int i = i_max + 1, j = n - 1; i < n/2 + 1; i++, j--)
            swap(a[i], a[j]);

		//vuvid
        for (int i=0;i<n;i++)
		{
			cout << a[i]<<" ";
		}
		cout<<endl;
	}
 
    system("pause");
    return 0;
}