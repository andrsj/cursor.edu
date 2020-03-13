#include <iostream>
#include "Header.h"

using namespace std;

void enqueue(int data, Item **MyItem)
{
	Item *temp=new Item;
	temp-> data = data;
	temp->Next = NULL;

	if ((*MyItem)->Front == NULL){
		(*MyItem)->Front = temp;
	} else
	{
		(*MyItem)->Rear->Next = temp;
	}

	(*MyItem)->Rear = temp;
}

void dequeue(int data, Item **MyItem)
{
	if ((*MyItem)->Front == NULL){ 
		cout << "Cherga porognya ";
		return;
	}
	else
	{
		Item *temp = (*MyItem)->Front; 
		(*MyItem)->Front = temp->Next; 
		delete temp; 
	}
}

void show(Item *MyItem) 
{
    Item *temp=new Item; 
	temp=MyItem->Front; 
               
    while (temp!=NULL)  
    {
		cout<<temp->data<<" "; 
        temp=temp->Next;
    }
}

void main()
{
    Item *MyItem=new Item; 
	MyItem->Front=NULL; 
	int number, element;

    cout << "Vvedit 1 shchob dodaty element v chergy\n";
    cout << "Vvedit 2 shchob vudalutu element z chergy\n";
    cout << "Vvedit 3 shchob vidobrazutu chergy\n";
	cout << "Vvedit 4 shchob vuytu z programu\n";

	for (int i = 1; i < 100; i++){
	cin >> number;

	switch (number)
	{
	case 1:
		cout << "Vvedit element yakuy hochete dodatu\n";
		cin >> element;
		enqueue(element,&MyItem);
		cout << "Cherga -> ";
		show(MyItem);
		break;
		
	case 2:
		dequeue(element,&MyItem);
		cout << "Cherga -> ";
		show(MyItem);
		break;

	case 3:
		cout << "Cherga -> ";
		show(MyItem);
		break;

	case 4:
		exit(0);
	}
	}
	system ("pause");
}