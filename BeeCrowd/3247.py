from collections import deque

def dpPath(obstacleGrid):
  rows = len(obstacleGrid)
  cols = len(obstacleGrid[0])
  dp = list(list(0 for i in range(cols)) for i in range (rows))
  flag = False
  
  # first row
  for i in range (cols):
    if flag or obstacleGrid[0][i] == 1:
      flag = True
      dp[0][i] = 0
    else:
      dp[0][i] = 1
      
  # first column
  flag = False
  for i in range (rows):
    if flag or obstacleGrid[i][0] == 1:
      flag = True
      dp[i][0] = 0
    else:
      dp[i][0] = 1
      
  for i in range(1,rows):
    for j in range(1,cols):
      if(obstacleGrid[i][j] == 1):
        dp[i][j] = 0
      else:
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) 
      
        
  return dp[rows-1][cols-1]

def bfs(grid):
  R, C = len(grid), len(grid[0])
  q = deque()
  vis = [[False]*R for i in range(C)]
  
  q.append((0,0))
  vis[0][0] = True
  while len(q):
    x, y = q.popleft()
  
    if(x,y) == (R-1,C-1): return True
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      new_x, new_y = x+dx, y+dy
      if 0 <= new_x < R and 0 <= new_y < C and not vis[new_x][new_y] and grid[new_x][new_y] == 0:
        vis[new_x][new_y] = True
        q.append((new_x, new_y))
        
  return False

# MAIN

grid = list()
n = int(input())
for i in range(n):
  s = input()
  s = s.replace(".", "0")
  s = s.replace("#", "1")
  line = list(int(char) for char in s)
  grid.append(line)
  
dpResult = dpPath(grid)  
  
if dpResult != 0:
  print(dpResult)
else:
  if bfs(grid): print("THE GAME IS A LIE")
  else: print("INCONCEIVABLE")
