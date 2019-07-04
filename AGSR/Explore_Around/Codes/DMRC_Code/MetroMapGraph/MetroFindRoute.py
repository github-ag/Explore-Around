def findRoute(graph, start, end, Route =[]):
    Route = Route + [start]
    if start == end:
        return Route
    for node in graph[start]:
        if node not in Route:
            newRoute = findRoute(graph, node, end, Route)
            if newRoute:
                return newRoute
            return None

def findAllRoutes(graph, start, end, Route =[]):
    Route = Route + [start]
    if start == end:
        return [Route]
    Routes = []
    for node in graph[start]:
        if node not in Route:
            newRoutes = findAllRoutes(graph, node, end, Route)
        for newRoute in newRoutes:
            Routes.append(newRoute)
    return Routes

def findShortestRoute(graph, start, end, Route =[]):
    Route = Route + [start]
    if start == end:
        return Route
    shortest = None
    for node in graph[start]:
        if node not in Route:
            newRoute = findShortestRoute(graph, node, end, Route)
            if newRoute:
                if not shortest or len(newRoute) < len(shortest):
                    shortest = newRoute
    return shortest
