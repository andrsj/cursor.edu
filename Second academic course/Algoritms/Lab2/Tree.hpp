#include "Node.hpp"

class Tree {
private:
    void destroyTree(Node* leaf);
    void insert(dataType key, Node* leaf);
    Node* search(dataType key, Node* leaf);

    void showTree(Node* leaf);

    void infixPrint(Node* leaf);
    void postfixPrint(Node* leaf);
    void prefixPrint(Node* leaf);

    Node* root;

public:
    Tree();
    ~Tree();

    void destroyTree();
    void insert(dataType key);
    Node* search(dataType key);

    void showTree();

    void infixPrint();
    void postfixPrint();
    void prefixPrint();

    Node* successorNodeBSD(Node* leaf);
    Node* predecessorNodeBSD(Node* leaf);
    void deleteNodeBSD(Node* leaf);
};
