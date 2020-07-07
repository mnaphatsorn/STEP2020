import math
from common import print_tour, read_input, format_tour

def getdistance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solver_greedy(cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = getdistance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour

def optimizetour(cities):
    N = len(cities)
    tour = solver_greedy(cities)
    next_cities=[0 for i in range(N)]
    for i in range(N-1):
        next_cities[tour[i]] =  tour[i+1]
    next_cities[tour[N-1]] =  tour[0]
    for k in range(5):
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
    for i in range(8):
        cities = read_input(f'input_{i}.csv')
        tour = optimizetour(cities)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')
