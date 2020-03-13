#include <iostream>

using namespace std;

struct Item
{
    int data; //значення
    Item *Next,*Head; //Голова стеку і вказівник на наступний елемент
};

void push(int data, Item **MyItem);
void pop(int data, Item **MyItem);
void show(Item *MyItem);