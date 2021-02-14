class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colour={i:-1 for i in range(len(graph))} #making all vertices uncoloured 
        
        def dfs(pos):
            for j in graph[pos]:     #Taking each adjacent vertex at a time
                if colour[j]==-1:    #If it is uncoloured, colour it with opposite colour of pos
                    colour[j]=1-colour[pos] 
                    temp=dfs(j)  # Colour all the adjacent vertices of j 
                    if not temp:
                        return False
                elif colour[j]==colour[pos]: #if the adjacent vertex pos & j are of the same colour
                    return False
            return True
            
            
        for i in range(len(colour)): # taking each vertex at a time
            if colour[i] == -1:    # if it is uncoloured, colour it
                colour[i]=0  
                result=dfs(i)   #Colour it's all adjacent vertices
            if not result :
                return False
        return True    
