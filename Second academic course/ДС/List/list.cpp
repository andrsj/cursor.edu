#include"stdafx.h"
#include <iostream>
#include "list.h"
Item *head, *temp, *first = NULL, *last = NULL;

void add_begin(datatype data)
{
    Item *temp = new Item;
    temp->data = data;
    temp->next = first;
    temp->previous = NULL;
    if (first != NULL) first->previous = temp; else last = temp;
    first = temp;
}

void add_end(datatype data)
{
    Item *temp = new Item;
    temp->data = data;
    temp->next = NULL;
    temp->previous = last;
    if (first != NULL) last->next = temp; else first = temp;
    last = temp;
}
void del_begin()
{
    if (first == NULL)
    {cout << "Spusok pustuy" << endl;return;}
    Item *temp = first;
    first = temp->next;
    if (first != NULL)first->previous = NULL; else last = NULL;
    delete temp;
}
void del_end()
{
    if (last == NULL)
    {
        cout << "Spusok pustuy" << endl;
        return;
    }
    Item *temp = last;
    last = temp->previous;
    if (first != NULL) last->next = NULL; else first = NULL;
    delete temp;
}
Item *search(datatype data)
{
    bool find = false;
    Item *temp = first;
    while (temp != NULL)
    {
        if (temp->data == data)
        {
            find = true;
            return temp;
        }
        temp = temp->next;
    }
    if (!find) return NULL;
}
void add_mid(datatype f_value, datatype newdata)
{  
    Item *pkey = NULL;
    pkey = search(f_value);
    if (pkey == NULL)
    {
        cout << "Element ne znaydeno" << endl;
        return;
    }
    if (pkey == last)
    {
        add_end(newdata);
        return;
    }
    Item *temp = new Item;
    temp->data = newdata;
    temp->next = pkey->next;
    temp->previous = pkey;
    pkey->next = temp;
    (temp->next)->previous = temp;
}
void del_mid(datatype data)
{
    Item *pkey = NULL;
    pkey = search(data);
    if (pkey == NULL)
    {
        cout << "Element ne znaydeno"<<endl;
        return;
    }
    if (pkey == first)
    {
        del_begin();
        return;
    }
    if (pkey == last)
    {
        del_end();
        return;
    }
    (pkey->previous)->next = pkey->next;
    (pkey->next)->previous = pkey->previous;
}
void show()
{
    Item *temp = first;
    while (temp != NULL)
    {
        cout << temp->data << endl;
        temp = temp->next;
    }
}
