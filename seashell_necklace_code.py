n = int(input())
graph = []

for i in range(n): 
    graph.append(input())

''' sample input
2
<>
<> answer: 4

'''

def find_max_length(graph):
    string_of_necklace = 0
    def dfs(n, graph, r, c, visited, path, current_max): 
        #track the movement of the algorithm 
        #print('(x, y):', (r, c), 'path', path)
        nonlocal string_of_necklace
        
        #if the string is balanced, it can return the maximum between the current path and the ongoing max length
        if graph[r][c] == '>' and is_balanced(path):
            current_max = max(len(path), string_of_necklace)
            #print('Path: ', path, 'Current max length:', current_max)
            string_of_necklace = current_max
            return 
        
        visited.add((r, c))
        #if it is not balanced, keep searching for more cells that are '>' until the string is balanced
        if graph[r][c] == '>' and not is_balanced(path): 
            for (rr, cc) in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]: 
                if 0<=rr<n and 0<=cc<n and (rr, cc) not in visited and graph[rr][cc] == '>': 
                    dfs(n, graph, rr, cc, visited.copy(), path+'>', current_max)
            
        if graph[r][c] == '<': 
            for (rr, cc) in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]: 
                if 0<=rr<n and 0<=cc<n and (rr, cc) not in visited: 
                    dfs(n, graph, rr, cc, visited.copy(), path+graph[rr][cc], current_max)
            
    dfs(len(graph), graph, 0, 0, set(()), '<', 0)
    return string_of_necklace
        
def is_balanced(string): 
    i, j = 0, len(string) - 1
    if (len(string)%2)!=0: 
        return False
    while j>i: 
        if string[i]!='<' or string[j]!='>': 
            return False
        i+=1
        j-=1
            
    return True
    
if graph[0][0] == '>':
    print(0)
else: 
    if find_max_length(graph) == None: 
        print(0)
    else: 
        print(find_max_length(graph))
