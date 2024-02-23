import vtk
import trimesh
import numpy as np
import matplotlib.pyplot as plt
from vtk.util.numpy_support import vtk_to_numpy
import cmocean
from functions import fixPlot
#
# USER INPUT DATA
#
file_path = '../fine/postProcessing/cuttingPlane/10000/U_cutz5.vtk'
obj_file = 'geoFiles/buildings_z5.stl'
#
# Read the data
#
reader = vtk.vtkPolyDataReader()
reader.SetFileName(file_path)
reader.Update()
polydata = reader.GetOutput()
points = polydata.GetPoints()
data = vtk_to_numpy(polydata.GetPointData().GetArray(0))
Umag = np.sqrt(data[:,0]**2 + data[:,1]**2+ data[:,2]**2)
x = vtk_to_numpy(points.GetData())
# Load an OBJ file
mesh = trimesh.load(obj_file)
# Get the x and y coordinates for the top view
xf = mesh.vertices[:, 0]
yf = mesh.vertices[:, 1]
#
# Plotting
#
fixPlot(thickness=1.5, fontsize=20, markersize=8, labelsize=15, texuse=True, tickSize = 15)
plt.figure(1,figsize=(10,8))
plt.tricontourf(x[:,0],x[:,1],Umag,cmap=cmocean.cm.thermal,levels=20)
plt.colorbar()
# Color the faces of the 3D mesh with black
for face in mesh.faces:
        # This is the most compute intensive line as it plots every face in the mesh.
        # So if you mesh is super dense then it can be an issue. User be warned!
        plt.fill(xf[face], yf[face], facecolor='gray', edgecolor='None', alpha=1.0)
plt.xlim([-500,500])
plt.ylim([-500,1000])
plt.show()