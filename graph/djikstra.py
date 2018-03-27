

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


processed = []

agraph ={}
agraph['start'] ={}
agraph['start']['a'] = 5
agraph['start']['b'] = 2
agraph['a'] ={}
agraph['a']['c'] = 4
agraph['a']['d'] = 2
agraph['b'] ={}
agraph['b']['a'] =8
agraph['b']['d'] =7
agraph['c'] ={}
agraph['c']['d'] =6
agraph['c']['finish'] =3
agraph['d'] ={}
agraph['d']['finish'] =1
agraph['finish'] ={}

acosts ={}
_infinity = float('inf')
acosts['a'] = 5
acosts['b'] = 2
acosts['c'] = _infinity
acosts['d'] = _infinity
acosts['finish'] = _infinity



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



def mimimumDistance(_node,costs,graph):
    while _node is not None:
        cost = costs[_node]
        neighbour = graph[_node]
        for n in neighbour.keys():
            newcost = cost +neighbour[n]
            if  costs[n] > newcost:
                costs[n] = newcost
        processed.append(_node)
        _node = find_lowest_cost_node(costs)

#_node = find_lowest_cost_node(acosts)
#mimimumDistance(_node,acosts,agraph)

print(acosts)

bgraph ={}
bgraph['start'] ={}
bgraph['start']['a'] = 10
bgraph['a'] ={}
bgraph['a'] ['b'] = 20
bgraph['b'] ={}
bgraph['b'] ['finish'] = 30
bgraph['b'] ['c'] = 1
bgraph['c'] ={}
bgraph['c']['a'] = 1
bgraph['finish'] ={}

ccosts ={}
ccosts['a'] = 10
ccosts['b'] =_infinity
ccosts['c'] = _infinity
ccosts['finish'] =_infinity
__node = find_lowest_cost_node(ccosts)
mimimumDistance(__node,ccosts,bgraph)
print('-----------------------------')
print(ccosts)