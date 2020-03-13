#ifndef LIST_H
#define LIST_H

typedef int datatype;

struct Item
{
    datatype data;
    Item* next;
    Item* previous; //у випадку двозв’язного списку
};
extern Item *head, *temp, *front, *rear, *first, *last;

void push(datatype data);
void pop();
void show();

void enqueue(datatype data);
void dequeue();
void show_2();

void DFS(datatype start, int n);
void recursDFS(datatype vertex,int **f);
void BFS(datatype start, int n);


#endif // LIST_H
