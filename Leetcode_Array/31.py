# Spiral Matrix III
# https://leetcode.com/problems/spiral-matrix-iii/

# input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],
# [3,2],[2,2],[1,2],[0,2],[4,5],[4,4],
# [4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],
# [4,0],[3,0],[2,0],[1,0],[0,0]]
#
#Given that:
rows = 5
cols = 6
rStart = 1
cStart = 4
             
ans = []  #let the answer is
left=cStart  # initial starting column number for left position
right=cStart+1 #initial starting column number for right position
top= rStart # initial starting row number for top position
bottom =rStart+1 #  # initial starting row number for bottom position

current = 1  #
move = 0     #

def inbound( r, c, rows, cols):         
    return 0<=r<rows and 0<=c<cols     #while row number is less than total rows and colmun number is less than total column numbers



while current <= rows*cols: #while current is less than row*column
    
    # fill top
    for i in range(left+move, right+1):
        if inbound(top, i, rows, cols):
            ans.append([top, i])
            current += 1
    left -= 1
    # fill right
    for i in range(top+1, bottom+1):
        if inbound(i, right, rows, cols):
            ans.append([i, right])
            current += 1
    top -= 1
    # fill bottom
    for i in range(right-1, left-1, -1):
        if inbound(bottom, i, rows, cols):
            ans.append([bottom, i])
            current += 1
    right += 1
    # fill left
    for i in range(bottom-1, top-1, -1):
        if inbound(i, left, rows, cols):
            ans.append([i, left])
            current += 1
    bottom += 1
    move = 1
    print(ans)



