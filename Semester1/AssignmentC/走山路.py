import heapq
direction=[[1,0],[-1,0],[0,1],[0,-1]]

def dick(x1,y1,x2,y2):
    q=[(0,x1,y1)]
    distance={(x1,y1):0}

    while q:
        heapq.heapify(q)
        energy,x,y = heapq.heappop(q)
        if (x,y)==(x2,y2):
            return energy
        
        for dx,dy in direction:
            nx,ny=x+dx,y+dy

            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] != "#":
                    total_energy = abs(int(matrix[nx][ny])-int(matrix[x][y]))+energy
                    if (nx,ny) not in distance or total_energy< distance[(nx,ny)]:
                        heapq.heappush(q,(total_energy,nx,ny))
                        distance[(nx,ny)]=total_energy

    return 'NO'



m,n,p=map(int,input().split())
matrix=[list(input().split()) for _ in range(m)]
test=[list(map(int,input().split())) for _ in range(p)]

for i in range(p):
   print(dick(test[i][0],test[i][1],test[i][2],test[i][3]))
