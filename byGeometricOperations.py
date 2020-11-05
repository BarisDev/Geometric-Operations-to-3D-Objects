##Author: Baris Yarar
##Num: 1306160048

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from itertools import combinations
import numpy as np
from numpy import sin, cos

def translate(verts,x,y,z):
    tMatrix=np.array([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])
    temp=[]
    products=[]
    #print(verts[0])
    #verts[0] += d
    for element in range(len(verts)):
        temp = np.array([verts[element][0],verts[element][1],verts[element][2],1])
        product = tMatrix.dot(temp)
        #print(product[element])
        temp = [product[0],product[1],product[2],product[3]]
        products.append(temp)
    #print(products)
    print("Translated")
    resetCoordinates(verts,products)

def scale(verts,x,y,z):
    sMatrix=np.array([[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]])
    temp=[]
    products=[]
    #print(verts[0])
    #verts[0] += d
    for element in range(len(verts)):
        temp = np.array([verts[element][0],verts[element][1],verts[element][2],1])
        product = sMatrix.dot(temp)
        #print(product[element])
        temp = [product[0],product[1],product[2],product[3]]
        products.append(temp)
    #print(products)
    print("Scaled")
    resetCoordinates(verts,products)

def rotate(verts,axis,alpha):
    theta = np.radians(alpha)
    if axis==z:
        rMatrix=np.array([[cos(theta),-1*sin(theta),0,0],[sin(theta),cos(theta),0,0],[0,0,1,0],[0,0,0,1]])
    elif axis==y:
        rMatrix=np.array([[cos(theta),0,sin(theta),0],[0,1,0,0],[-1*sin(theta),0,cos(theta),0],[0,0,0,1]])
    elif axis==x:
        rMatrix=np.array([[1,0,0,0],[0,cos(theta),-1*sin(theta),0],[0,sin(theta),cos(theta),0],[0,0,0,1]])
    temp=[]
    products=[]
    #print(verts[0])
    #verts[0] += d
    for element in range(len(verts)):
        temp = np.array([verts[element][0],verts[element][1],verts[element][2],1])
        product = rMatrix.dot(temp)
        #print(product[element])
        temp = [product[0],product[1],product[2],product[3]]
        products.append(temp)
    print("Rotated")
    resetCoordinates(verts,products)

def rotate2(verts,axis1,axis2,alpha):
    if axis1==z and axis2==y:
       rotate(verts,z,alpha)
       rotate(verts,y,alpha)
    if axis1==x and axis2==y:
       rotate(verts,x,alpha)
       rotate(verts,y,alpha)
    if axis1==x and axis2==z:
       rotate(verts,x,alpha)
       rotate(verts,z,alpha)    
    if axis1==y and axis2==z:
       rotate(verts,y,alpha)
       rotate(verts,z,alpha)
    if axis1==y and axis2==x:
       rotate(verts,y,alpha)
       rotate(verts,x,alpha)
    if axis1==z and axis2==x:
       rotate(verts,z,alpha)
       rotate(verts,x,alpha)    

def rotate3(verts,axis1,axis2,axis3,alpha):
    rotate(verts,axis1,alpha)    
    rotate(verts,axis2,alpha)    
    rotate(verts,axis3,alpha)    

def resetCoordinates(vertices, newVertices):
    for i in range(len(vertices)):
        vertices[i] = newVertices[i]
        x[i] = newVertices[i][0]
        y[i] = newVertices[i][1]
        z[i] = newVertices[i][2]
    print("Reset Completed")

def draw(vertices):
    #vertices array's 4th elements needed for matrix product,
    #poly3dcollection declines more than 3 element.
    for i in vertices:
        i.pop(3)
    poly3d = []
    comb=[]
    comb = combinations(vertices,3)
    for i in list(comb):
        temp = [i[0],i[1],i[2]]
        poly3d.append(temp)
    ax.scatter(x,y,z,c='r')
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='b', linewidths=1, alpha=0.5))
    plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

temp=[]
vertices=[]

# corner coordinates x1,y1,z1 = x[1],y[1],z[1]
# this is a cube, you can change coordinates and draw your own 3d object
x = [0, 1, 1, 1, 0, 0, 1, 0]
y = [0, 0, 1, 0, 1, 1, 1, 0]
z = [0, 0, 0, 1, 0, 1, 1, 1]
t = [1, 1, 1, 1, 1, 1, 1, 1] # for translations

for index in range(len(x)):
    temp = [x[index],y[index],z[index],t[index]]
    vertices.append(temp)

###Translation methods must call below here! 
##There are 3 methods for Rotation: 
#rotate2: around 2 axis
#rotate3: around 3 axis, (output will change depend on axis order)
#Example usage for all methods:
#translate(vertices,1,0,0)
#scale(vertices,2,2,2)
#rotate(vertices,x,120)
#rotate2(vertices,y,z,60)
#rotate3(vertices,x,z,y,240)
draw(vertices)
