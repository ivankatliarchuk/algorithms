# graph table
graph = {}
graph['you'] = ['alice', 'bob', 'claire']

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
# costs table
# represent infinity
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
# parent table
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

print(graph['start'].keys())
print(graph)
print(costs)
print(parents)
# swap with set
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    # go through each node
    for node in costs:
        cost = costs[node]
        # its the lowest cost so far and hasn't been processed yet
        if cost < lowest_cost and node not in processed:
            # set the new lowest cost node
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# find the lowest cost node that you haven't processed yet
node = find_lowest_cost_node(costs)
print("{0} -->first lowest node<--  and {1}".format(node, processed))

# if you processed all the nodes, this while loop is done
while node is not None:
    cost = costs[node]
    neigbours = graph[node]
    # go through all the neigbours of this n node
    for n in neigbours.keys():
        new_cost = cost + neigbours[n]
        # if it's cheaper to get to this neigbour by doing through this node..
        if costs[n] > new_cost:
            # update the cost for this neigbour
            costs[n] = new_cost
            # this node becomes the new parent for this neigbour
            parents[n] = node
    # mark the node as processed
    processed.append(node)
    node = find_lowest_cost_node(costs)

print('{} the price.'.format(costs))
print('{} the path.'.format(parents))
