# Geometric Operations to 3D Objects
 This code applies Rotate, Scale, Translate operations to 3D objects.
## Code Explanation
x, y, z are coordinate arrays for cube. t is needed for translations.<br>You can also change these coordinates for your shape.
```
x = [0, 1, 1, 1, 0, 0, 1, 0]
y = [0, 0, 1, 0, 1, 1, 1, 0]
z = [0, 0, 0, 1, 0, 1, 1, 1]
t = [1, 1, 1, 1, 1, 1, 1, 1]
```
`draw(vertices)` method draws your 3d object.
![Cube](https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube.png?raw=true)

`translate(vertices,x,y,z)` method translates your 3d object.
![cube translated 1 unit on x axis.](https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-translate.png?raw=true)

`scale(vertices,x,y,z)` method scales your 3d object.
![cube 2x scaled](https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-scale.png?raw=true)

`rotate(verts,axis,alpha)` method rotates your 3d object in 1 axis.
![`rotate(vertices,x,120)` cube rotated 120 degrees around x axis.](https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-1-axis.png?raw=true)

`rotate2(verts,axis,axis,alpha)` method rotates your 3d object around 2 axis.
![`rotate2(vertices,y,z,60)` cube rotated 60 degrees around y and z axes.](https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-2-axis.png?raw=true)

`rotate3(verts,axis,axis,axis,alpha)` method rotates your 3d object around 3 axis.
![`rotate3(vertices,x,z,y,240)` cube rotated 240 degrees around all axes.](https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-3-axis.png?raw=true)

<p align="center">
  <img src="https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-3-axis.png?raw=true" />
</p>
