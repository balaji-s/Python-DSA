
'''
first create a graph of mapping values
between nodes and edges
'''
graph ={}
graph['start'] ={}
graph['start']['a']= 6
graph ['start']['b'] =2
graph['a'] ={}
graph['a']['finish'] =1
graph['b'] ={}
graph['b']['a'] =3
graph ['b']['finish'] = 5
graph['finish'] ={}

'''
then calculate the costs for each node
'''
infinity = float('inf')
costs ={}
costs['a'] =6
costs['b'] =2
costs['finish'] = infinity

'''
map which node is connected to which node
'''
parents = {}
parents['a'] ='start'
parents['b'] ='start'
parents['finish'] = None

processed = []

def find_lowest_cost_node(_costs):
    '''
    finds the lowest cost for the first time and then next lowest and so on
    '''
    lowestcost = float('inf')
    lowestcostnode = None
    for node in _costs:
        cost = _costs[node]
        if cost < lowestcost and node  not in processed:
            lowestcost = cost
            lowestcostnode = node
    return lowestcostnode


_node = find_lowest_cost_node(costs)

while _node is not None:
    cost = costs[_node]
    neighbour = graph[_node]
    for n in neighbour.keys():
        newcost = cost +neighbour[n]
        if costs[n] > newcost:
            costs[n] = newcost
            parents[n] = _node
    processed.append(_node)
    _node = find_lowest_cost_node(costs)

print(costs, parents, graph)

