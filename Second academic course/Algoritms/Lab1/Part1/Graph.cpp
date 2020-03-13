#include "Graph.hpp"
#include "DisjointSets.hpp"

Graph::Graph(int V, int E) {
    this->V = V;
    this->E = E;
}

void Graph::addEdge(int from, int to, int weight) {

    std::pair<int, std::pair<int, int> > edge = std::make_pair(weight, std::make_pair(from, to));

    this->edges.push_back(edge);
}

int Graph::kruskalMST() {

    int minimunWeightSum = 0;

    std::stable_sort(this->edges.begin(), this->edges.end());

    DisjoitSets disjointSets(V);

    std::vector< std::pair<int, std::pair<int, int> > >::iterator iterator;

    for (iterator = this->edges.begin(); iterator != this->edges.end(); iterator++) {
        
        int from = iterator->second.first;
        int to = iterator->second.second;

        int setFrom = disjointSets.find(from);
        int setTo = disjointSets.find(to);

        if (setFrom != setTo) {

            std::cout << from + 1 << " -- " << to + 1 << '\n';

            minimunWeightSum += iterator->first;

            disjointSets.merge(setFrom, setTo);
        }
    }

    return minimunWeightSum;
}