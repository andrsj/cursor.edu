#include <cstddef>
#include <iostream>

#include "Tree.hpp"

Tree::Tree() {
    root = nullptr;
}

Tree::~Tree() {
    destroyTree();
}

void Tree::destroyTree(Node* leaf) {

    if (leaf != nullptr) {

        destroyTree(leaf->left);
        destroyTree(leaf->right);

        delete leaf;
    }
}

void Tree::insert(dataType key, Node* leaf) {

    if (key < leaf->key) {

        if (leaf->left != nullptr) {
            insert(key, leaf->left);
        } else {
            leaf->left = new Node;
            leaf->left->key = key;
            leaf->left->left = nullptr;
            leaf->left->right = nullptr;
            leaf->left->parent = leaf;
        }
    } else if (key >= leaf->key) {

        if (leaf->right != nullptr) {
            insert(key, leaf->right);
        } else {
            leaf->right = new Node;
            leaf->right->key = key;
            leaf->right->left = nullptr;
            leaf->right->right = nullptr;
            leaf->right->parent = leaf;
        }
    }
}

Node* Tree::search(dataType key, Node* leaf) {

    if (leaf != nullptr) {

        if (key == leaf->key) {
            return leaf;
        }

        if (key < leaf->key) {
            return search(key, leaf->left);
        } else {
            return search(key, leaf->right);
        }

    } else {
        return nullptr;
    }
}

void Tree::insert(int key) {

    if (root != nullptr) {
        insert(key, root);
    } else {
        root = new Node;
        root->key = key;
        root->left = nullptr;
        root->right = nullptr;
        root->parent = nullptr;
    }
}

void Tree::showTree(Node* leaf) {

    if (leaf != nullptr) {
        std::cout << leaf->key << ", ";
        showTree(leaf->left);
        showTree(leaf->right);
    }
}

void Tree::infixPrint(Node* leaf) {

    if (leaf != nullptr) {
        infixPrint(leaf->left);
        std::cout << leaf->key << ", ";
        infixPrint(leaf->right);
    }
}

void Tree::postfixPrint(Node* leaf) {

    if (leaf != nullptr) {
        infixPrint(leaf->left);
        infixPrint(leaf->right);
        std::cout << leaf->key << ", ";
    }
}

void Tree::prefixPrint(Node* leaf) {

    if (leaf != nullptr) {
        std::cout << leaf->key << ", ";
        infixPrint(leaf->left);
        infixPrint(leaf->right);
    }
}

Node* Tree::search(int key) {
    return search(key, root);
}

void Tree::destroyTree() {
    destroyTree(root);
}

void Tree::showTree() {
    showTree(root);
    std::cout << '\n';
}

void Tree::infixPrint() {
    infixPrint(root);
    std::cout << '\n';
}

void Tree::postfixPrint() {
    postfixPrint(root);
    std::cout << '\n';
}

void Tree::prefixPrint() {
    prefixPrint(root);
    std::cout << '\n';
}

Node* Tree::successorNodeBSD(Node* leaf) {

    if (leaf->right != nullptr) {

        Node* previous = leaf->right;

        while(previous->left != nullptr) {
            previous = previous->left;
        }

        return previous;
    } else {

        Node* previous = leaf->parent;

        while (previous != nullptr && leaf == previous->right) {
            leaf = previous;
            previous = previous->parent;
        }

        return previous;
    }
}

Node* Tree::predecessorNodeBSD(Node* leaf) {

    if (leaf->left != nullptr) {

        Node* next = leaf->left;

        while (next->left != nullptr) {
            next = next->left;
        }

        return next;
    } else {

        Node* previous = leaf->parent;

        while (previous != nullptr && leaf == previous->right) {
            leaf = previous;
            previous = previous->parent;
        }

        return previous;
    }
}

void Tree::deleteNodeBSD(Node* leaf) {

    if (leaf->left == nullptr && leaf->right == nullptr) {

        if (leaf == root) {
            delete root;
            return;
        }

        if (leaf->parent->left == leaf) {
            leaf->parent->left = nullptr;
        } else if (leaf->parent->right == leaf) {
            leaf->parent->right = nullptr;
        }

        delete leaf;
    } else if (leaf->left != nullptr || leaf->right != nullptr) {

        Node* next;

        if (leaf->left != nullptr) {
            next = leaf->left;
        } else {
            next = leaf->right;
        }

        if (leaf == root) {
            root = next;
            delete leaf;
        } else {

            if (leaf->parent->left == leaf) {
                leaf->parent->left = next;
            } else {
                leaf->parent->right = next;
            }

            next->parent = leaf->parent;

            delete leaf;
        }
    } else {

        Node* term = successorNodeBSD(leaf);

        leaf->key = term->key;
        deleteNodeBSD(term);
    }
}
