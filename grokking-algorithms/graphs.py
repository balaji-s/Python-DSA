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