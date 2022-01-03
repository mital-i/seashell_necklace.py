n = int(input())
graph = []

for i in range(n): 
    graph.append(input())

''' sample input
2
<>
<> answer: 4

'''

''' sample input (code not working) 
4
<<>>
<><<
<<><
>>><
answer should be: 8
my answer: 6

'''

def find_max_length(graph):
    string = None
    def dfs(n, graph, r, c, visited, path, current_max): 
        print(r, c, "hi", path)
        nonlocal string         
        if graph[r][c] == '>' and is_balanced(path):
            string = path
            return 
        
        visited.add((r, c))
        if graph[r][c] == '>' and not is_balanced(path): 
            for (rr, cc) in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]: 
                if 0<=rr<n and 0<=cc<n and (rr, cc) not in visited and graph[rr][cc] == '>': 
                    dfs(n, graph, rr, cc, visited.copy(), path+'>', current_max)
            
        if graph[r][c] == '<': 
            for (rr, cc) in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]: 
                if 0<=rr<n and 0<=cc<n and (rr, cc) not in visited: 
                    dfs(n, graph, rr, cc, visited.copy(), path+graph[rr][cc], current_max)
            
    dfs(len(graph), graph, 0, 0, set(()), '<', 0)
    return string
        
def is_balanced(string): 
    i, j = 0, len(string) - 1
    while j>i: 
        if string[i]!='<' or string[j]!='>': 
            return False
        i+=1
        j-=1
            
    return True
    
if graph[0][0] == '>':
    print(0)
else: 
    print(find_max_length(graph))
