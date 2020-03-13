struct DisjoitSets {   
    int *parent;
    int *rank;

    int n;

    DisjoitSets(int n) {
        
        this->n = n;

        this->parent = new int[n + 1];
        this->rank = new int[n + 1];

        for (int i = 0; i < n; ++i) {
            rank[i] = 0;
            parent[i] = i;
        }
    }

    int find(int v) {
        
        if (v != parent[v]) {
            parent[v] = find(parent[v]);
        }

        return parent[v];
    }

    void merge(int x, int y) {
        
        x = find(x);
        y = find(y);

        if (rank[x] > rank[y]) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }

        if (rank[x] == rank[y]) {
            rank[y]++;
        }
    }
};