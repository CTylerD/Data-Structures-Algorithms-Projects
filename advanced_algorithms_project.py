import heapq


def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    # build hash table of straight line distance from each node to goal
    dists_to_goal = node_to_goal_dists(M, goal)
    # build hash table of distances between all adjacent nodes
    dists_between_ints = intersection_dists(M)
    shortest_path = travel_map(M, start, goal, dists_to_goal,
                               dists_between_ints)
    return shortest_path


def travel_map(M, start, goal, dist_to_goal, dist_between_ints):
    explored = []
    # frontier is a min heap comprised of tuples containing:
    # (dist traveled + est dist, curr node val, dist traveled, [path traveled])
    frontier = []

    # initialize frontier heap with start
    heapq.heappush(frontier, (0 + dist_to_goal[start], start, 0, [start]))
    
    while goal not in explored:
        min_frontier = heapq.heappop(frontier)
        curr_node = min_frontier[1]
        dist_traveled = min_frontier[2]
        path_traveled = min_frontier[3]

        for adj_node in dist_between_ints[curr_node]:
            g_dist_traveled = (dist_traveled +
                              dist_between_ints[curr_node][adj_node])
            h_dist_to_goal = dist_to_goal[adj_node]
            g_h_total = g_dist_traveled + h_dist_to_goal
            updated_path = path_traveled + [adj_node]

            new_frontier_state = (g_h_total, adj_node, g_dist_traveled,
                                  updated_path)
            heapq.heappush(frontier, new_frontier_state)

        explored.append(curr_node)
        
    return path_traveled


def find_distance(node_a, node_b):
    dist = ((node_a[0] - node_b[0])**2 +
            (node_a[1] - node_b[1])**2)**(1/2)
    
    return dist


def node_to_goal_dists(M, goal):
    dists = {}

    for node in range(len(M.intersections)):
        dist = find_distance(M.intersections[node], M.intersections[goal])
        dists[node] = dist

    return dists


def intersection_dists(M):
    dists = {}

    for node in range(len(M.intersections)):
        temp_dists = {}
        for adj in M.roads[node]:
            dist = find_distance(M.intersections[node], M.intersections[adj])
            temp_dists[adj] = dist
        dists[node] = temp_dists

    return dists
