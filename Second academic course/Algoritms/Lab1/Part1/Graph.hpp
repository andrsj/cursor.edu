#include <algorithm>
#include <iostream>
#include <vector>

class Graph {
    int V;
    int E;

    std::vector< std::pair< int , std::pair<int, int> > > edges;

public:
    Graph(int V, int E);
    void addEdge(int from, int to, int weight);
    
    int kruskalMST();
};
