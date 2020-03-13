#include <iostream>

#include "Tree.hpp"

int main() {

    int keys[] = {10, 6, 14, 5, 8, 11, 18};

    Tree* tree = new Tree();

    for (int number : keys) {
        tree->insert(number);
    }

    std::cout << "Prefix print:\n";
    tree->prefixPrint();
    std::cout << '\n';

    std::cout << "Infix print:\n";
    tree->infixPrint();
    std::cout << '\n';

    std::cout << "Postfix print:\n";
    tree->postfixPrint();
    std::cout << '\n';

    Node* nodeToFind = tree->search(6);

    if (nodeToFind != nullptr) {

        Node* successorNode = tree->successorNodeBSD(nodeToFind);
        Node* predecessorNode = tree->predecessorNodeBSD(nodeToFind);

        std::cout << "Parent of node " << nodeToFind->key << ": " << nodeToFind->parent->key << '\n';
        std::cout << "Successor node of node " << nodeToFind->key << ": " << successorNode->key << '\n';
        std::cout << "Predecessor node of node " << nodeToFind->key << ": " << predecessorNode->key << '\n';

        tree->deleteNodeBSD(nodeToFind);

        std::cout << "Tree after deleting node " << nodeToFind->key << '\n';
        tree->showTree();
    }

    delete tree;

    return 0;
}
