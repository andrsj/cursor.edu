#include "stdafx.h"
#include <iostream>
using namespace std;
typedef char datatype;

struct Item
{	datatype data;
	Item* next;
};
Item *head, *temp; 

void push(datatype data)
{	Item *temp = new Item;
	temp->data = data;
	temp->next = head;
	head = temp;
}

void pop()
{	if (head != NULL)
	{		Item *temp = head;
		head = temp->next;
		delete temp;	}
}

void show()
{	
	Item *temp = head;
	if(temp==NULL)
		cout << endl << "���� ������!" << endl << endl; else { cout << endl << "������ �����:" << endl;
	while (temp != NULL)
	{	cout << temp->data << std::endl;
	temp = temp->next;}}
}


struct Item_Q
{	datatype data;
	Item_Q* next;
};
Item_Q *temp_Q, *front = NULL, *rear = NULL;
void enqueue(datatype data)
{	Item_Q *temp_Q = new Item_Q;
	temp_Q->data = data;
	temp_Q->next = NULL;
	if (front == NULL)	front = temp_Q;	else rear->next = temp_Q;rear = temp_Q;}
void dequeue()
{	if (front != NULL)
	{Item_Q *temp_Q = front;front = temp_Q->next;delete temp_Q;}
}
void show_Q()
{	
	Item_Q *temp_Q = front;
	if(temp_Q==NULL)
		cout << endl << "����� �����!" << endl << endl; else {cout << endl << "������ �����:" << endl;
	while (temp_Q != NULL)
	{cout << temp_Q->data << endl;temp_Q = temp_Q->next;}}
}


struct Item_D
{
	datatype data;
	Item_D* next;
	Item_D* previous;
};
Item_D *temp_D, *first = NULL, *last = NULL;
void add_begin(datatype data)
{	Item_D *temp_D = new Item_D;
	temp_D->data = data;
	temp_D->next = first;
	temp_D->previous = NULL;
	if (first != NULL)
	{first->previous = temp_D;}else{last = temp_D;}first = temp_D;}
void add_end(datatype data)
{	Item_D *temp_D = new Item_D;
	temp_D->data = data;
	temp_D->next = NULL;
	temp_D->previous = last;
	if (first != NULL)last->next = temp_D;else	{first = temp_D;}
	last = temp_D;}
void del_begin()
{	if (first == NULL)
	{cout << "������ ������!" << endl;return;}
	Item_D *temp_D = first;
	first = temp_D->next;
	if (first != NULL)first->previous = NULL;
	else	last = NULL;	delete temp_D;}
void del_end()
{	if (last == NULL)
	{cout << "������ ������!" << endl;return;}
	//if(first!=NULL)
	Item_D *temp_D = last;last = temp_D->previous;
if (first != NULL)last->next = NULL;else	first = NULL;delete temp_D;}

Item_D *search(datatype data)
{	bool find = false;
	Item_D *temp_D = first;
	while (temp_D != NULL)
	{	if (temp_D->data == data){find = true;cout << temp_D;return temp_D;}
		temp_D = temp_D->next;	}
	if (!find){return NULL;}
}
void add_mid(datatype olddata, datatype newdata)
{	Item_D *pkey = NULL;
	pkey = search(olddata);
	if (pkey == NULL){cout << "������� �� ��������!" << endl;return;}
	if (pkey == last){add_end(newdata);return;}
	Item_D *temp_D = new Item_D;
	temp_D->data = newdata;
	temp_D->next = pkey->next;
	temp_D->previous = pkey;
	pkey->next = temp_D;
	(temp_D->next)->previous = temp_D;}
void del_mid(datatype data)
{	Item_D *pkey = NULL;
	pkey = search(data);
	if (pkey == NULL){cout << "������� �� ��������!\n";	return;}
	if (pkey == first){del_begin();cout << "��������!\n";return;}
	if (pkey == last){del_end();cout << "��������!\n";return;}
	(pkey->previous)->next = pkey->next;
	(pkey->next)->previous = pkey->previous;}
void show_D()
{	Item_D *temp_D = first;
	if(temp_D==NULL)
		cout << endl << "������ ������!" << endl << endl; else {cout << endl << "������:" << endl;
	while (temp_D != NULL)
	{	cout << temp_D->data << endl;
	temp_D = temp_D->next;}}
}

int _tmain(int argc, _TCHAR* argv[])
{
	setlocale(LC_ALL, "ukr");
	cout << "������ �� ����� ����� ����i�� 11, �������� �i ����� - 12, ������� ������ ����� ����� - 13, " << endl;
	cout << "������ �� ����� ����� ����i�� 21, �������� � ����� - 22, ������� ������ ����� ����� - 23," << endl;
	cout << "������ �� ������� �����'������ ������ - 1, � ���� �i���� - 2, " << endl;
	cout << "�������� �� ������� - 3, � �i��i - 4, �������� ������ - 5, " << endl;
	cout <<	"������ ������� - 6, �������� ������� �i��� ����������� - 7, �������� ���� - 8: "<< endl;
	while(true)
	{   
		int n;
		cin >> n;
		cout << endl;
		switch(n){	
			case 1: cout << "����i�� ����� : ";
				datatype num_f;
					cin >> num_f;
					add_begin(num_f);
			        break;
			case 2: cout << "����i�� ����� : ";
				datatype num_l;
					cin >> num_l;
					add_end(num_l);
					break;
			case 3: del_begin();
					break;
			case 4: del_end();
					break;
			case 5: show_D();break;
			case 6: cout << "����i�� ����� : ";
				datatype num_s;
					cin >> num_s;
					cout << (search(num_s) ? "��������!\n" : "�� ��������!\n");break;
			case 7: datatype as, an;
					cout << "����i�� ����� ��� ������:";
					cin >> as;
					cout << "����i�� ����� : ";
					cin >> an;
					add_mid(as, an);
					break;
			case 8: datatype dd;
					cout << "����i�� ������� ���� �������� : ";
					cin >> dd;
					del_mid(dd);
					break;

			case 11: cout << "����i�� ����� : ";
				datatype num;
					cin >> num;
					push(num); 
					cout << endl;
					break;
			case 12: pop();
					break;
			case 13: show();
					break;
			case 21: cout << "����i�� ����� : ";
				datatype num_Q;
					cin >> num_Q;
					enqueue(num_Q);
					cout << endl;
			        break;
			case 22: dequeue();
					 break;
			case 23: show_Q();
					 break;
			default: cout << "������� ���i��� �����!" << endl;
		}
	}

	return 0;
}

