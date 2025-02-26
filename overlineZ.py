from paraview.simple import *
import math  # Import the math module to use cos and sin functions

# Disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Load the OpenFOAM data
foamfoam = OpenFOAMReader(registrationName='foam.foam', FileName='C:5\\foam.foam')
UpdatePipeline(time=4500.0, proxy=foamfoam)

# Define the coordinates for each z-pencil in the first quadrant
points = [
    (0, 0),                 # Origin
    (0, 3),                 # y = 3
    (0, 6),                 # y = 6
    (0, 9),                 # y = 9
    (12 * math.sin(math.radians(45)), 12 * math.sin(math.radians(45))),  # x = y = 12sin(45)
    (3 * math.sin(math.radians(45)), 3 * math.sin(math.radians(45))),        # x = y = 3sin(45)
    (6 * math.sin(math.radians(45)), 6 * math.sin(math.radians(45))),        # x = y = 6sin(45)
    (9 * math.sin(math.radians(45)), 9 * math.sin(math.radians(45)))         # x = y = 9sin(45)
]

# Loop through each point and create a PlotOverLine filter
for i, (x, y) in enumerate(points):
    # Create PlotOverLine filter at the specified (x, y) coordinate
    plotOverLine = PlotOverLine(registrationName=f'PlotOverLine{i+1}', Input=foamfoam)
    plotOverLine.Point1 = [x, y, -12.5]  # Start of the line at z = -12.5
    plotOverLine.Point2 = [x, y, 50.0]   # End of the line at z = 50.0
    UpdatePipeline(time=6500.0, proxy=plotOverLine)

    # Save the data for each line
    SaveData(f'C:/Users/Usama/Desktop/pipesim/ico_175/overline_z{i+1}.csv', proxy=plotOverLine,
             PointDataArrays=['UMean', 'UPrime2Mean', 'pMean', 'pPrime2Mean', 's1Mean', 's1Prime2Mean', 's2', 's2Mean', 's2Prime2Mean', 
                              's3', 's3Mean', 's3Prime2Mean', 's4', 's4Mean', 's4Prime2Mean', 's5', 's5Mean', 's5Prime2Mean', 
                              's6', 's6Mean', 's6Prime2Mean', 'vtkValidPointMask'],
             AddTime=1)
