from Queue import Queue
import numpy as np
def neighbours(AMat,i):
    nbrs = []
    (rows,cols) = AMat.shape
    for j in range(cols):
        if AMat[i,j] == 1:
            nbrs.append(j)
    return(nbrs)
def BFS(Amat,v):
    rows,columns = Amat.shape
    visited = {}
    for i in range(rows):
        visited[i] = False
    q = Queue()
    visited[v] = True
    q.addq(v)
    while not q.isempty():
        j = q.delq()
        for k in neighbours(Amat,j):
            if not visited(k):
                visited[k] = True
                q.addq(k)
    return visited        

def BFS_path(Alist:dict,v):
    visited,parent = dict(),dict()
    for i in Alist.keys():
        visited[i] = False
        parent[i] = -1
    q = Queue()
    visited[v] = True
    q.addq(v)
    while not q.isempty():
        j = q.delq()
        for k in Alist[j]:
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.addq(k)
    return visited,parent
            