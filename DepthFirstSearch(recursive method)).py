#depthfirstsearch
def depthfirstsearch(graph,start):
    stack=[start]
    print(start)
    for x in graph[start]:
        depthfirstsearch(graph,x)





graph = { 'a':['b','c'] , 'b':['d'] , 'c' :['e'] ,'d' : ['f'],'e':[],'f':[]   }
start='a'
traversal = depthfirstsearch(graph,start)

