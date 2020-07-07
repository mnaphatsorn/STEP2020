import math
from common import print_tour, read_input, format_tour

def getdistance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def alldistance(cities):
    N = len(cities)
    distance = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
                if i == j:
                    distance[i][j]=float('inf')
                    continue
                distance[i][j]= distance[j][i]=getdistance(cities[i], cities[j])
    return distance 

def root(node,parent):
    while node != parent[node]:
        node = parent[node]
    return node
    
def union(a,b,parent):
    a = root(a,parent)
    b = root(b,parent)
    parent[a]=b

#create a minimun spanning tree by Kruskal's algorithm
def kruskalMST(cities): 
    N = len(cities)
    # Initialize sets of disjoint sets 
    distance = alldistance(cities)
    parent = [i for i in range(N)]
    MST = [[]for i in range(N)]
    
    # Include minimum weight edges one by one  
    edge_count = 0
    while edge_count < N - 1: 
        min = float('inf')
        a = -1
        b = -1
        for i in range(N): 
            for j in range(N): 
                #to aviod any cyclic path, add an edge  when 2 nodes does not have the same root 
                if root(i,parent) != root(j,parent) and distance[i][j] < min: 
                    min = distance[i][j] 
                    a = i 
                    b = j 
        union(a, b,parent) 
        MST[a].append(b)
        MST[b].append(a)
        edge_count += 1
    return MST, parent

#find a path that travel to all nodes based on MST
def findtour(cities): 
    N = len(cities)
    mst, parent =  kruskalMST(cities)
    tour = []
    r = root(0, parent)
    q = [r]
    while len(tour)< N:
        curr = q.pop()
        if curr not in tour:
            tour.append(curr)
            for v in mst[curr]:
                q.append(v)
    return tour

#optimize any crossing path to the shorter path
def optimizepath(cities):
    N = len(cities)
    tour = findtour(cities)
    next_cities=[0 for i in range(N)]
    for i in range(N-1):
        next_cities[tour[i]] =  tour[i+1]
    next_cities[tour[N-1]] =  tour[0]
    for k in range(1):
        for i in range(N):
            for j in range(i+1, N):
                node1 = i
                node2 = j
                next_1 = next_cities[node1]
                next_2 = next_cities[node2]
                distance1 = getdistance(cities[node1], cities[next_1]) + getdistance(cities[node2], cities[next_2])
                distance2 = getdistance(cities[node1], cities[node2]) + getdistance(cities[next_1], cities[next_2])
                if distance1 > distance2 :
                    point = next_cities[node1]
                    next_cities[node1] = node2
                    previous_points = next_cities[node2]
                    while point != node2:
                            next_point = next_cities[point]
                            next_cities[point] =  previous_points
                            previous_points = point
                            point = next_point
                    next_cities[point] =  previous_points
                    # print(next_cities)
    path =[]
    path.append(0)
    startpoint=next_cities[0]
    while startpoint !=  0 :
        path.append(startpoint)
        startpoint = next_cities[startpoint]
    # print(path)
    return path


if __name__ == '__main__':
    for i in range(7):
        cities = read_input(f'input_{i}.csv')
        tour = optimizepath(cities)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')
