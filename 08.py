class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.num_components -= 1
            return True
        return False

    def get_components(self):
        components = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        return components

# PART 1
pos = [list(map(int, p.split(","))) for p in open("08.txt").read().strip().split("\n")]
dsu = DSU(len(pos))
dists = []
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        dist = ((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2 + (pos[i][2] - pos[j][2]) ** 2)
        dists.append((dist, i, j))
dists.sort()
for i in range(1000):
    dist, x, y = dists[i]
    dsu.union(x, y)
components = dsu.get_components()
component_sizes = [len(c) for c in components.values()]
component_sizes.sort(reverse=True)
component_size_prod = 1
for size in component_sizes[:3]:
    component_size_prod *= size
print(component_size_prod)

# PART 2
dsu = DSU(len(pos))
dist_idx = 0
while dsu.num_components > 1:
    edge = dists[dist_idx]
    if dsu.union(edge[1], edge[2]):
        a, b = pos[edge[1]][0], pos[edge[2]][0]
    dist_idx += 1
print(a * b)