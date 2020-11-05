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
`draw(vertices)` method draws your 3d object.)
<p align="center">
  <img src="https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube.png?raw=true" />
</p>

`translate(vertices,x,y,z)` method translates your 3d object.

<p align="center">
  <img src="https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-translate.png?raw=true" />
</p>

`scale(vertices,x,y,z)` method scales your 3d object.

<p align="center">
  <img src="https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-scale.png?raw=true" />
</p>

`rotate(verts,axis,alpha)` method rotates your 3d object in 1 axis.

<p align="center">
  <img src="https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-1-axis.png?raw=true" />
</p>

`rotate2(verts,axis,axis,alpha)` method rotates your 3d object around 2 axis.

<p align="center">
  <img src="https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-2-axis.png?raw=true" />
</p>

`rotate3(verts,axis,axis,axis,alpha)` method rotates your 3d object around 3 axis.

<p align="center">
  <img src="https://github.com/BarisDev/Geometric-Operations-to-3D-Objects/blob/main/cube-3-axis.png?raw=true" />
</p>
