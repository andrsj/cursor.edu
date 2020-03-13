#include <iostream>
#include <fstream>

#include "list.h"

using namespace std;

int main()
{
    ifstream f1("input.txt");
    datatype start;
    datatype vertex;
    int n,p;
    int **f = new int* [8];
    for (int i=0; i<8; i++)
        f[i] = new int [8];
    int a[8][8] = {
        {0,1,0,1,1,0,0,0},
        {1,0,1,0,1,0,0,0},
        {0,1,0,0,1,0,0,0},
        {1,0,0,0,1,1,0,0},
        {1,1,1,1,0,0,0,0},
        {0,0,0,1,0,0,1,1},
        {0,0,0,0,0,1,0,1},
        {0,0,0,0,0,1,1,0}
    };
    for (int i=0; i<8; i++)
    {
        for (int j=0; j<8; j++)
        {
            f[i][j] = a[i][j];
        }
    }

    cout<<"Enter 1 if you need DFS \nEnter 2 if you need recursDFS \nEnter 3 if you need BFS\nExit 4"<<endl;
    cin>>p;
    if (p==1)
    {
        cout<<"Start vertex: ";
        cin>>start;
        cout<<"Size matrix: ";
        cin>>n;
        cout<<"DFS "<<"Number Stac"<<endl;
        DFS(start - 1, n);
    } else if (p==2){
        cout<<"Start vertex: ";
        cin>>vertex;
        cout<<"Size matrix: ";
        cin>>n;
        cout<<"DFS "<<"Number Stac"<<endl;
        recursDFS(vertex - 1, f);
    } else if (p==3){
        cout<<"Start vertex: ";
        cin>>start;
        cout<<"Size matrix: ";
        cin>>n;
        cout<<"BFS "<<"Number Stac"<<endl;
        BFS(start - 1, n);
    }
}
