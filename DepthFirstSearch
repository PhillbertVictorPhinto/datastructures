def depthfirstsearch(graph,start):
    stack=[start]
    while(stack):
        current = stack.pop()
        print(current)
        for nodes in graph[current]:
            stack.append(nodes)
    return




graph = { 'a':['b','c'] , 'b':['d'] , 'c' :['e'] ,'d' : ['f'],'e':[],'f':[]   }
start='a'
traversal = depthfirstsearch(graph,start)
