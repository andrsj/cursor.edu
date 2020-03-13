#ifndef LIST_H
#define LIST_H

#include <iostream>
using namespace std;

typedef int datatype;

struct Item
{	int data;
    Item* next;
    Item* previous;
};
extern Item *head, *temp, *first, *last;

void add_begin(int data);
void add_end(int data);
void del_begin();
void del_end();
Item *search(int data);
void add_mid(int olddata, int newdata);
void del_mid(int data);
void show();

#endif // LIST_H
