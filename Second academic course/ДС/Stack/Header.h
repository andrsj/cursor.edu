#include <iostream>

using namespace std;

struct Item
{
    int data; //��������
    Item *Next,*Head; //������ ����� � �������� �� ��������� �������
};

void push(int data, Item **MyItem);
void pop(int data, Item **MyItem);
void show(Item *MyItem);