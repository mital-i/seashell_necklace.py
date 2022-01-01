n = int(input())
graph = []

for i in range(n): 
    graph.append(input())

def solve(grid, length, n, current_shell):
        ans = None
        def dfs_left(r, c, necklace_length, current_shell):
            #we don't need a visited array. 
            #If we change the visited coordinate to '.' we won't visit it again since we only travel to coordinates that are '<'
            graph[r][c] = '.'
            nonlocal ans
            if ans:
                return
                    
            #if the necklace_length reached the size "length" then return the length, otherwise it would return None 
            if necklace_length == length: 
                ans = path
                return
                
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= rr < n and 0 <= cc < n:
                    if grid[rr][cc]==current_shell:
                        dfs_left(rr, cc, necklace_length + 1, current_shell)
                            
        #path length starts with length 1 because the shell at (0,0) has to be "<" otherwise 
        #path length defaults to zero
        dfs_left(0, 0, 1, current_shell)
        return ans

#if the first shell is ">" then a necklace can't be made at all so the length of the necklace would be zero
if graph[0][0] == '>':
    print(0)
else: 
    #check if there is a seashell path of this length made up of '<'
    print(solve(graph, 4, n, '<'))
    #check if there is a seashell path of this length made up of '>'
    #how do I do this? I need to make sure the dfs starts from the last coordinate that the dfs function ended at
