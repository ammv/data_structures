graph_lib = {}

graph = {}
graph['a'] = ['b', 'c']
graph['b'] = ['c']
graph['c'] = ['f']
graph['f'] = ['k']
graph['k'] = []

graph_lib['abc'] = graph

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

graph_lib['Object X'] = graph

graph = {}
graph['start'] = ['finish']
graph['finish'] = ['start']

graph_lib['start-finish'] = graph

graph = {}
graph['Bob'] = ['Way 0', 'Way 1', 'Way 2', 'Way 3']

graph['Way 0'] = ['Way 1', 'Way 4']
graph['Way 1'] = ['Way 2', 'Way 5']
graph['Way 2'] = ['Way 3', 'Way 6']
graph['Way 3'] = ['Way 0', 'Way 7']

graph['Way 4'] = ['Way 5']
graph['Way 5'] = ['Way 6', 'Way 8', 'Way 9']
graph['Way 6'] = ['Way 7']
graph['Way 7'] = ['Way 4', 'Way 10', 'Way 11']

graph['Way 8'] = ['Bob']
graph['Way 9'] = ['Bob']
graph['Way 10'] = ['Bob']
graph['Way 11'] = ['Bob']

graph_lib['Center'] = graph
