#15. [Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/)





rows = 2
cols = 2
rCenter = 0
cCenter = 1

def dist(point):
        pi, pj = point
        return abs(pi - rCenter) + abs(pj - cCenter)

               

points = [(i, j) for i in range(rows) for j in range(cols )]


print(sorted(points, key=dist))