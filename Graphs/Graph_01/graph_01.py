'''
github/ammv/data_structures
author: Artem Momatov
vk: vk.com/mimo113
'''
from graphlib.graphlib import graph_lib

def filter(object):
    '''removes duplicate items from the list'''
    new_object = []
    for i in object:
        if i not in new_object:
            new_object.append(i)
    return new_object

def show(object):
    '''show list'''
    return ''.join(str(i) + '\n' for i in object)

def get_short_way(childs, start, find):
    '''
    find the shortest path from start to find
    find - the element we are looking for in the graph
    '''
    way = [find]
    i = 0
    while find != start:
        object = childs[i]
        if find in object[1]:
            way.append(object[0])
            find = object[0]
            i = 0
        else:
            i += 1
            if i == len(childs):
                return False
    return way[::-1]

def graph_find(graph, start, find):
    '''find algorythm - search in width'''
    queue = [start] + graph[start]
    childs = []
    history = []
    while queue:
        object = queue.pop(0)
        if object == find:
            history.append(object)
            return True, history, filter(childs)
        else:
            history.append(object)
            childs.append([object, graph[object]])
            queue.extend(graph[object])
    return False, history, filter(childs)

if __name__ == '__main__':
    name, start, find = 'Center', 'Bob', 'Way 11'
    x = graph_find(graph_lib[name], start, find)
    print('\n')
    print('Result:', x[0],'\n')
    print('History:\n' + show(x[1]))
    print('Childs:\n' + show(x[2]))
    print('Short way:\n' + show(get_short_way(x[2], start, find)))