import numpy as np
class Ant():
    def __init__(self):
        pass

    def ant_tour(self,t_matrix,adj_matrix,h_matrix,Q,a,b):
        rows = len(adj_matrix)
        cols = len(adj_matrix[0])
        # initialize tour
        length = 0
        o_nodes = [x for x in range(0,len(adj_matrix)) if True]
        l_p_matrix = np.zeros((rows,cols))

        # Starting position
        starting_node = np.random.randint(0,rows+1)
        route = [starting_node]
        o_nodes.remove(starting_node)

        current_index = starting_node

        while len(o_nodes) > 0:
            next_node = next_transition(t_matrix,h_matrix, current_index,o_nodes,a,b)
            route.append(next_node)
            length += adj_matrix[current_index][next_node]
            current_index = next_node
            o_nodes.remove(next_node)

        # Close the link from last node to starting node
        length += adj_matrix[current_index][starting_node]
    
        local_t_matrix = local_pheromone_matrix(Q,length,route,rows,cols)

        
        return route, length, local_t_matrix





def next_transition(pheromone_matrix, heuristic_matrix, at_row,o_nodes,a,b):
    # Probability of each transition
    # The most probable value is the point we go to next.
    probability_row = probability_matrix(at_row,o_nodes,pheromone_matrix, heuristic_matrix,a,b)

    best_fit_index = 0
    current_most_probable = probability_row[0]
    # Find best edge
    for i in range(0,len(probability_row)):
        if probability_row[i] > current_most_probable:
            current_most_probable = probability_row[i]
            best_fit_index = i

    return best_fit_index

def local_pheromone_matrix(Q, l,route,rows,cols):
    lp_matrix = np.zeros((rows,cols))

    current_point = route[0]
    for i in range(1,len(route)):
        lp_matrix[current_point][route[i]] = Q / l
        current_point = start_point

    # Make last link
    lp_matrix[current_point][route[0]] = Q / l

    return lp_matrix


def in_path(n, o_nodes):
    for i in o_nodes:
        if n == i:
            return True
    return False

def probability_matrix(row_index, o_nodes,p_matrix, h_matrix,a,b):
    cols = len(p_matrix[0])

    sum_rows = probability_sum(p_matrix, h_matrix, row_index, o_nodes,a,b)

    probability_row = []
    for c in range(0,cols):
        p_cell = p_matrix[row_index][c]
        h_cell = h_matrix[row_index][c]

        val = probability_cell(sum_rows,p_cell,h_cell,a,b)
        probability_row.append(val)

    return probability_row

def probability_sum(p_matrix, h_matrix, row_index, o_nodes,a,b):
    cols = len(p_matrix[0])

    sum_rows = 0
    for c in range(0, cols):
        p_cell = p_matrix[row_index][c]
        h_cell = h_matrix[row_index][c]
        if in_path(c, o_nodes):
            sum_rows += pow(p_cell,a) * pow(h_cell,b)
    return sum_rows

def probability_cell(sum_rows, p_cell, h_cell, a, b):
    probability = pow(p_cell,a) * pow(h_cell,b) / sum_rows

    return probability
