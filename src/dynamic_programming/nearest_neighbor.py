import json


# Nearest neighbour algorithm (greedy algorithm) done non-recursively
# It doesn't guarantee a solution, will return True if solution is found,
# otherwise will return False
def shortest_path_nn(firstNode, cities, path=[]):
    # use cities by value, not by referance
    cities = dict(cities)
    for city in cities:
        cities[city] = dict(cities[city])

    distance = 0

    # append first node
    path.append(firstNode)

    while len(path) < len(cities):
        # choose nearest nonvisited city
        if cities[path[-1]]:
            nearestCity = min(cities[path[-1]], key=cities[path[-1]].get)
        else:
            return False
        while nearestCity in path:
            del cities[path[-1]][nearestCity]
            if cities[path[-1]]:
                nearestCity = min(cities[path[-1]], key=cities[path[-1]].get)
            else:
                return False

        # if such city is found update distance and path
        distance += cities[path[-1]][nearestCity]
        path.append(nearestCity)

    if firstNode in cities[path[-1]]:
        distance += cities[path[-1]][firstNode]
        path.append(firstNode)
    else:
        return False

    print("Solution found: ", path)
    print("Distance: ", distance)

    return True


if __name__ == '__main__':
    # load cities
    with open('cities.json') as json_data:
        cities = json.load(json_data)

    print("Nearest neighbour algorithm:")
    for city in cities:
        print("Start: ", city)
        if not shortest_path_nn(city, cities, []):
            print("Solution not found")