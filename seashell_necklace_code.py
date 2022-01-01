n = int(input())
graph = []

for i in range(n): 
    graph.append(input())

def solve(grid, length, n, current_shell):
        ans = None
        def dfs_left(r, c, path, visited, current_shell):
                nonlocal ans
                if ans:
                    return
                    
                if len(path) == length: 
                    ans = path
                    return
                
                visited.add((r, c))
                #r,c = 0, 2
                for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= rr < n and 0 <= cc < n:
                        if (rr, cc) not in visited and grid[rr][cc]==current_shell:
                            dfs_left(rr, cc, path + grid[r][c], visited.copy(), current_shell)
                            

        dfs_left(0, 0, '<', set(), current_shell)
        return ans

visited = set(())

if graph[0][0] == '>':
    print(0)
else: 
    #check if there is a seashell path of this length made up of '<'
    print(solve(graph, 4, n, '<'))
    #check if there is a seashell path of this length made up of '>'
    
