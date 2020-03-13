#include <iostream>

const int V = 9;

int findMinimumKey(int key[], bool mstSet[]) {

    int minIndex;
    int min = INT_MAX;

    for (int i = 0; i < V; i++) {
        if (mstSet[i] == false && key[i] < min) {
            min = key[i];
            minIndex = i;
        }
    }

    return minIndex;
}

int printOutputMST(int parent[], int graph[V][V]) {
    
    std::cout << "Edge" << " - " << "Weight" << '\n'; 

    for (int i = 1; i < V; i++) {
        std::cout << parent[i] << " - " << i << " \t" << graph[i][parent[i]] << '\n';
    }

    return 0;
}

void primMST(int graph[V][V]) {
    
    int parent[V];
    int key[V]; 
    bool mstSet[V];  
  
    for (int i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = false; 
    }
  
    key[0] = 0;      
    parent[0] = -1;
  
    for (int count = 0; count < V - 1; count++) { 

        int minimumKey = findMinimumKey(key, mstSet); 
  
        mstSet[minimumKey] = true; 
  
        for (int i = 0; i < V; i++) {
            if (graph[minimumKey][i] && mstSet[i] == false && graph[minimumKey][i] < key[i]) {
                parent[i] = minimumKey;
                key[i] = graph[minimumKey][i];
            }
        } 
    }

    printOutputMST(parent, graph);
}

int main() {

    int graph[V][V] = {
        {0, 4, 0, 0, 0, 0, 0, 8, 0},
        {4, 0, 8, 0, 0, 0, 0, 11, 0},
        {0, 8, 0, 7, 0, 4, 0, 0, 2},
        {0, 0, 7, 0, 9, 14, 0, 0, 0},
        {0, 0, 0, 9, 0, 10, 0, 0, 0},
        {0, 0, 4, 14, 10, 0, 2, 0, 0},
        {0, 0, 0, 0, 0, 2, 0, 1, 6},
        {8, 11, 0, 0, 0, 0, 1, 0, 7},
        {0, 0, 2, 0, 0, 0, 6, 7, 0}
    };

    primMST(graph);

    return 0;
}