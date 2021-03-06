import matplotlib.pyplot as pl
import numpy as np
import scipy as sp
import scipy.spatial
import sys

eps = sys.float_info.epsilon
eps = 0.1
n_towers = 100
towers = np.random.rand(n_towers, 2)
bounding_box = np.array([0., 1., 0., 1.]) # [x_min, x_max, y_min, y_max]

def in_box(towers, bounding_box):
    return np.logical_and(np.logical_and(bounding_box[0] <= towers[:, 0],
                                         towers[:, 0] <= bounding_box[1]),
                          np.logical_and(bounding_box[2] <= towers[:, 1],
                                         towers[:, 1] <= bounding_box[3]))


def antDistance(ant1, ant2):
    distance = (ant2[1]-ant1[1])**2 + (ant2[0]-ant1[0])**2
    return distance

def voronoi(towers, bounding_box):
    # Select towers inside the bounding box
    i = in_box(towers, bounding_box)
    # Mirror points
    points_center = towers[i, :]
    points_left = np.copy(points_center)
    points_left[:, 0] = bounding_box[0] - (points_left[:, 0] - bounding_box[0])
    points_right = np.copy(points_center)
    points_right[:, 0] = bounding_box[1] + (bounding_box[1] - points_right[:, 0])
    points_down = np.copy(points_center)
    points_down[:, 1] = bounding_box[2] - (points_down[:, 1] - bounding_box[2])
    points_up = np.copy(points_center)
    points_up[:, 1] = bounding_box[3] + (bounding_box[3] - points_up[:, 1])
    points = np.append(points_center,
                       np.append(np.append(points_left,
                                           points_right,
                                           axis=0),
                                 np.append(points_down,
                                           points_up,
                                           axis=0),
                                 axis=0),
                       axis=0)
    # Compute Voronoi
    vor = sp.spatial.Voronoi(points)
    #print(len(vor.point_region))
    # Filter9 regions
    regions = []
    indices = []
    for region in range(len(vor.regions)):
        flag = True
        for index in vor.regions[region]:
            if index == -1:
                flag = False
                break
            else:
                x = vor.vertices[index][0]
                y = vor.vertices[index][1]
                if not(bounding_box[0] - eps <= x and x <= bounding_box[1] + eps and
                       bounding_box[2] - eps <= y and y <= bounding_box[3] + eps):
                    flag = False
                    break
        if vor.regions[region] != [] and flag !=False:
            regions.append(vor.regions[region])
            #print(region,vor.point_region[region])
            
    nn = []
    clusterlist = []
    #print(nn)
    for region in range(len(regions)):
        nearestneighbour = 100
        clusters = [region]
        #nnindex = 0
        for neighbours in range(len(regions)):
            
            if neighbours != region:
                dist = antDistance(vor.points[region],vor.points[neighbours])
                if dist < 9:
                    clusters.append(neighbours)
    
                if dist < nearestneighbour:
                    nearestneighbour = dist
                    #nnindex = neighbours
        
        nn.append(nearestneighbour**0.5)
        clusterlist.append(clusters)
    vor.clusters = clusterlist
    vor.nearest_neighbour = nn
    vor.filtered_points = points_center
    
    vor.filtered_regions = regions
    
    return vor
'''
def centroid_region(vertices):
    # Polygon's signed area
    A = 0
    # Centroid's x
    C_x = 0
    # Centroid's y
    C_y = 0
    for i in range(0, len(vertices) - 1):
        s = (vertices[i, 0] * vertices[i + 1, 1] - vertices[i + 1, 0] * vertices[i, 1])
        A = A + s
        C_x = C_x + (vertices[i, 0] + vertices[i + 1, 0]) * s
        C_y = C_y + (vertices[i, 1] + vertices[i + 1, 1]) * s
    A = 0.5 * A
    C_x = (1.0 / (6.0 * A)) * C_x
    C_y = (1.0 / (6.0 * A)) * C_y
    return np.array([[C_x, C_y]])



fig = pl.figure()
ax = fig.gca()
vor = voronoi(towers, bounding_box)
ax.plot(vor.points[0,0], vor.points[0,1], 'go')
# Plot initial points
ax.plot(vor.filtered_points[0, 0], vor.filtered_points[0, 1], 'b.')
# Plot ridges points
for region in vor.filtered_regions:
    vertices = vor.vertices[region, :]
    ax.plot(vertices[:, 0], vertices[:, 1], 'go')
# Plot ridges
for region in vor.filtered_regions:
    vertices = vor.vertices[region + [region[0]], :]
    ax.plot(vertices[:, 0], vertices[:, 1], 'k-')
# Compute and plot centroids
centroids = []
for region in vor.filtered_regions:
    vertices = vor.vertices[region + [region[0]], :]
    centroid = centroid_region(vertices)
    centroids.append(list(centroid[0, :]))
print(centroids[0][0])
ax.plot(centroid[0][0], centroid[0][1], 'r.')

ax.set_xlim([-0.1, 1.1])
ax.set_ylim([-0.1, 1.1])
pl.savefig("bounded_voronoi.png")
pl.show()
#sp.spatial.voronoi_plot_2d(vor)

'''

