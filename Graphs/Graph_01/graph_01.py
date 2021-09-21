'''
github/ammv/data_structures
author: Artem Momatov
vk: vk.com/mimo113
'''

graph_lib = {} #for storing graphs

graph = {}
graph['a'] = ['b', 'c']
graph['b'] = ['c']
graph['c'] = ['f']
graph['f'] = ['k']
graph['k'] = []

graph_lib[str(len(graph_lib.keys()))] = graph

graph = {}
graph['Object 1(HEAD)'] = ['Object 2', 'Object 3']
graph['Object 2'] = ['Object 6']
graph['Object 3'] = ['Object 5']
graph['Object 5'] = ['Object 6']
graph['Object 6'] = ['Object 4']
graph['Object 4'] = ['Object 7', 'Object 8']
graph['Object 7'] = ['Object X']
graph['Object 8'] = ['Object 9']
graph['Object 9'] = ['Object 2']

graph_lib[str(len(graph_lib.keys()))] = graph

graph = {}
graph['start'] = ['finish']
graph['finish'] = ['start']

graph_lib[str(len(graph_lib.keys()))] = graph

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
    while find != start:
        object = childs.pop(-1)
        if find in object[1]:
            way.append(object[0])
            find = object[0]
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
    x = graph_find(graph_lib['1'], 'Object 1(HEAD)', 'Object X')
    print('\n')
    print('Result:', x[0],'\n')
    print('History:\n' + show(x[1]))
    print('Childs:\n' + show(x[2]))
    print('Short way:\n' + show(get_short_way(x[2], 'Object 1(HEAD)', 'Object X')))