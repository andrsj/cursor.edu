#include "list.h"

#include <fstream>
#include <iostream>

using namespace std;

Item *head, *temp, *front, *rear, *first, *last;

datatype visited[8];
datatype dfsnumber[8];

void push(datatype data)
{
    Item *temp = new Item;
    temp->data = data;
    temp->next = head;
    head = temp;
}

void pop()
{
    if (head == NULL)
    {
        cout<<"UPS"<<endl;
        return;
    }
    Item *temp = head;
    head = temp->next;
    delete temp;
}

void show()
{
    Item *temp = head;
    while (temp != NULL)
    {
        cout<<temp->data;
        temp = temp->next;
    }

}

void enqueue(datatype data)
{	Item *temp = new Item;
    temp->data = data;
    temp->next = NULL;
    if (front == NULL) front = temp; else rear->next = temp;
    rear = temp;
}

void dequeue()
{	if (front != NULL)
    {
        Item *temp = front;
        front = temp->next;
        delete temp;
    } else
    {
        cout<<"UPS"<<endl;
        return;
    }
}

void show_2()
{
    Item *temp = front;
    while (temp != NULL)
    {
        cout<<temp->data;
        temp = temp->next;
    }
}

void DFS(datatype start, int n/*, int *a*/)
{
    int dfs = 0;
    datatype visited[n];
    datatype dfsnumber[n];
    visited[start] = true;
    dfsnumber[start] = ++dfs;
    push(start);
    cout<<' '<<start+1<<"    "<<dfsnumber[start]<<"      ";
    show();
    cout<<endl;
    int a[n][n] = {
        {0,1,0,1,1,0,0,0},
        {1,0,1,0,1,0,0,0},
        {0,1,0,0,1,0,0,0},
        {1,0,0,0,1,1,0,0},
        {1,1,1,1,0,0,0,0},
        {0,0,0,1,0,0,1,1},
        {0,0,0,0,0,1,0,1},
        {0,0,0,0,0,1,1,0}
    };


    while(head != NULL)
    {
        for (int i=0; i<n; i++)
        {
            if((a[head->data][i] /*!= true*/) && (visited[i] != true))
            {
                visited[i] = true;
                dfsnumber[i] = ++dfs;
                //cout<<i<<' '<<dfsnumber[i]<<endl;
                cout<<' '<<i+1<<"    "<<dfsnumber[i]<<"      ";

                push(i);

                show();
                cout<<endl;
            }
        }
        cout<<" -    -      ";
        show();
        cout<<endl;
        pop();

    }

//    cout<<"DFS "<<"Number"<<endl;
//    for (int i=0; i<n; i++)
//    {
//        cout<<dfsnumber[i]<<' '<<i+1;
//        cout<<endl;
//    }
}

int dfs = 0;

void recursDFS(datatype vertex, int **f)
{

    int n = 8;
    visited[vertex] = true;

    dfsnumber[vertex] = ++dfs;

    cout<<' '<<vertex+1<<"   "<<dfsnumber[vertex]<<"      ";
    push(vertex);
    //    int a[n][n] = {
    //        {0,1,1,1,0,0,1,1},
    //        {1,0,0,0,0,0,1,1},
    //        {1,0,0,0,0,0,0,0},
    //        {1,0,0,0,1,1,0,0},
    //        {0,0,0,1,0,1,0,0},
    //        {0,0,0,1,1,0,0,0},
    //        {1,1,0,0,0,0,0,1},
    //        {1,1,0,0,0,0,1,0}
    //    };

    //    for (int i=0; i<8; i++)
    //    {
    //        for (int j=0; j<8; j++)
    //        {
    //            cout<<f[i][j]<<' ';
    //        }
    //        cout<<endl;
    //    }

    //    while (head != NULL)
    //    {
    //        for (int i=0; i<n; i++)
    //        {
    //            if (/*(f[head->data][i]) &&*/ (!visited[i]))
    //            {
    //                recursDFS(i, f);
    //            }
    //        }
    //        pop();
    //    }


    show();
    cout<<endl;
    for (int i=0; i<8; i++)
    {

        if (f[vertex][i] && !visited[i])
        {
            recursDFS(i, f);
            //cout<<"i = "<<vertex<<' '<<dfsnumber[i]<< endl;
        }
    }
    pop();
    cout<<" -   -      ";
    show();
    cout<<endl;



    //    for (int i=0; i<n; i++)
    //    {
    //        cout<<i+1<<' '<<dfsnumber[i];
    //        cout<<endl;
    //    }
}

void BFS(datatype start, int n)
{
    int bfs = 0;
    datatype visited[n];
    datatype bfsnumber[n];
    visited[start] = true;
    bfsnumber[start] = ++bfs;
    enqueue(start);
    cout<<' '<<start+1<<"    "<<bfsnumber[start]<<"     ";
    show_2();
    cout<<endl;
    int a[n][n] = {
        {0,1,0,1,1,0,0,0},
        {1,0,1,0,1,0,0,0},
        {0,1,0,0,1,0,0,0},
        {1,0,0,0,1,1,0,0},
        {1,1,1,1,0,0,0,0},
        {0,0,0,1,0,0,1,1},
        {0,0,0,0,0,1,0,1},
        {0,0,0,0,0,1,1,0}
    };


    while(front != NULL)
    {
        for (int i=0; i<n; i++)
        {
            if((a[front->data][i]) && (visited[i] != true))
            {
                visited[i] = true;
                bfsnumber[i] = ++bfs;
                cout<<' '<<i+1<<"    "<<bfsnumber[i]<<"     ";

                enqueue(i);
                show_2();
                cout<<endl;
            }
        }
        dequeue();
        cout<<" -    -     ";
        show_2();
        cout<<endl;
    }

//    for (int i=0; i<n; i++)
//    {
//        cout<<i+1<<' '<<bfsnumber[i];
//        cout<<endl;
//    }

}
