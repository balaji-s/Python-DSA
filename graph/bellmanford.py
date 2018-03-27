graph = {}
graph['start'] ={}
graph['start']['a'] =  2
graph['start']['b']= 2
graph['a'] ={}
graph['a']['c'] =2
graph['a']['finish'] = 2
graph['b'] = {}
graph['b']['a'] = 2
graph['c'] = {}
graph['c'] ['b'] = -1
graph['c']['finish'] = 2
graph['finish'] ={}

costs ={}
costs['start'] =0
costs['a'] = float('inf')
costs['b '] =float('inf')
costs['c'] = float('inf')
costs['finish'] = float('inf')

def bellmanFord(vertices, costs, graph):
    for i in range(vertices - 1):
        for key in graph.keys():
           for k in graph[key]:
               if costs[key] != float('inf') and costs[k] > costs[key]+graph[key][k]:
                   costs[k] = costs[key] + graph[key][k]
    return costs

ygraph = {}
ygraph['s'] ={}
ygraph['s']['a'] =10
ygraph['s']['e']  = 8
ygraph['a'] = {}
ygraph['a']['c'] =2
ygraph['b'] = {}
ygraph['b']['a']  = 1
ygraph['c'] ={}
ygraph['c']['b'] = -2
ygraph['d'] ={}
ygraph['d']['c'] = -1
ygraph['d'] ['a'] = -4
ygraph['e'] = {}
ygraph['e']['d'] = 1

ycosts = {}
ycosts['s'] = 0
ycosts['a'] =float('inf')
ycosts['b'] =float('inf')
ycosts['c'] =float('inf')
ycosts['d'] =float('inf')
ycosts['e'] =float('inf')
bellmanFord(6,ycosts,ygraph)
print(ycosts)