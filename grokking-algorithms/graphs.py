from collections import deque

graph = {}

graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def  mango_seller(takes_dict):
    while takes_dict:
        person = takes_dict.popleft()

        if person[-1] == 'm':
            return person + " is the mango seller"
        else:
            print(person)
            takes_dict += graph[person]
    return "there is no mango seller"

mango_seller(graph)