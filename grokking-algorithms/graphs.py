from collections import deque


graph = {}

graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thon', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thon'] = []
graph['jonny'] = []



def  mango_seller(person):
    takes_dict = deque();
    takes_dict += person
    searched = []
    while takes_dict:
        person = takes_dict.popleft()
        if person not in searched:
            if person[-1] == 'm':
                return person + " is the mango seller"
        else:
            searched.append(person)
            takes_dict += graph[person]
    return "there is no mango seller"

print(mango_seller(graph))

'''
dijkstra algorithm
'''
#first connect the dots using dictionary
dgraph = {}
dgraph['start'] ={}
dgraph['start']['a'] = 6
dgraph['start']['b'] = 2
dgraph['a'] ={}
dgraph['a']['finish'] = 1
dgraph ['b'] ={}
dgraph['b']['a'] = 3
dgraph['b']['finish'] = 5
dgraph['finish'] ={}

#then calculate the costs from start to the next connecting points

costs = {}
infinity = float('inf')
costs['a'] = 6
costs['b'] = 2
costs['finish'] = infinity

#convert the parents of node into dictionary

parents = {}
parents ['a'] ='start'
parents['b'] ='start'
parents['finish'] =None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs :
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not  None:
    cost = costs[node]
    neighbours = dgraph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(node)

