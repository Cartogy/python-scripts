import numpy as np
import ant

# All paths are likely
def initialize_pheromone(rows,cols):
    matrix = []
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            pheromone_value = 0
            if r != c:
                pheromone_value = 1
            row.append(pheromone_value)
        matrix.append(row)

    return matrix

def initialize_heuristic(adj_matrix):
    rows = len(adj_matrix)
    cols = len(adj_matrix[0])

    matrix = []
    for r in range(0,rows):
        row = []
        for c in range(0,cols):
            heuristic_value = 0
            if r != c:
                heuristic_value = 1.0 / adj_matrix[r][c] 
            row.append(heuristic_value)
        matrix.append(row)
    return matrix


def ant_colony(adj_matrix, Q,p,a,b,iterations,num_ants):
    rows = len(adj_matrix)
    cols = len(adj_matrix[0])
    
    forager = ant.Ant()

    # T matrix
    # Initiate pheromone matrix
    pheromone_matrix = np.array(initialize_pheromone(rows, cols))
    # H
    # How likely a path is
    heuristic_matrix = initialize_heuristic(adj_matrix)
    route_best = []
    length_best = 0
    for t in range(0,iterations):
        local_pheromone = np.zeros((rows,cols))
        for b in range(0, num_ants):
            route, length, lp_matrix_b = forager.ant_tour(pheromone_matrix,adj_matrix,heuristic_matrix,Q,a,b)
            if length < length_best:
                route_best = route
                length_best = length
            local_pheromone += lp_matrix_b
        pheromone_matrix = update_pheromone_matrix(pheromone_matrix,local_pheromone,p)
    return route_best, length_best



    # One single ant


# Point of view from an ant:
## Where do I go next, given I am at position X

## Output: Row index. Next point to go to


def update_pheromone_matrix(p_matrix, total_local_pheromones,p):

    pheromone_evaporation = (1-p) * p_matrix

    return pheromone_evaporation + total_local_pheromones






#         A B C D
graph = [
         [0,2,8,1], #A
         [2,0,6,3], #B
         [8,6,0,4], #C
         [1,3,4,0], #D
        ]
test_adj_matrix = np.array(graph)

ant_colony(test_adj_matrix,10,0.5,1,1,4,1)
