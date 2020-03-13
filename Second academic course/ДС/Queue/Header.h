struct Item
{
    int data;
    Item *Next,*Front, *Rear; 
};

void enqueue(int data, Item **MyItem);
void dequeue(int data, Item **MyItem);
void show(Item *MyItem);