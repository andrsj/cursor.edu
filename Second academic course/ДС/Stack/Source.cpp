#include <iostream>
#include "Header.h"

using namespace std;

void push(int data, Item **MyItem)
{
    Item *temp=new Item;
    temp->data=data;
    temp->Next=(*MyItem)->Head;
    (*MyItem)->Head=temp;
}

void pop(int data, Item **MyItem)
{
	if ((*MyItem)->Head == NULL){ 
		cout << "Stek porogniy ";
		return;
	}
	else
	{
		Item *temp = (*MyItem)->Head; 
		(*MyItem)->Head = temp->Next; 
		delete temp; 
	}

}

void show(Item *MyItem)
{
    Item *temp=new Item;
    temp=MyItem->Head;
             
    while (temp!=NULL) 
    {
		cout<<temp->data<<" ";
        temp=temp->Next;
    }
}

void main()
{
    Item *MyItem=new Item;
    MyItem->Head=NULL; 
	int number, element;

    cout << "Vvedit 1 shchob dodaty element v steck\n";
    cout << "Vvedit 2 shchob vudalutu element z steck\n";
    cout << "Vvedit 3 shchob vidobrazutu steck\n";
	cout << "Vvedit 4 shchob vuytu z programu\n";

	for (int i = 1; i < 100; i++){
	cin >> number;

	switch (number)
	{
	case 1:
		cout << "Vvedit element yakuy hochete dodatu\n";
		cin >> element;
		push(element,&MyItem);
		cout << "Steck -> ";
		show(MyItem);
		break;
		
	case 2:
		pop(element,&MyItem);
		cout << "Steck -> ";
		show(MyItem);
		break;

	case 3:
		cout << "Steck -> ";
		show(MyItem);
		break;

	case 4:
		exit(0);
	}
	}
	system ("pause");
}