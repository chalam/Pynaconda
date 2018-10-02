# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html#scipy.spatial.ConvexHull
# convex hull is represented as a set of N-1 dimensional simplices, which in 2-D means line segments
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
points = np.random.rand(30, 2) # 30 rand points in 2D
hull = ConvexHull(points)
print('hull simplices', hull.simplices)
#plot it
convex_hull_plot_2d(hull)
#
# import matplotlib.pyplot as plt
# plt.plot(points[:,0], points[:,1], 'o')
# for simplex in hull.simplices:
#     plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
#
# plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
# plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
# plt.show()
#
