import plotly.offline as py
import numpy as np
from numpy import cos, sin, pi
from plotly.graph_objs import Mesh3d

phi = np.linspace(0, 2*pi)
theta = np.linspace(-pi/2, pi/2)
phi, theta=np.meshgrid(phi, theta)

orientation=45*pi/180;

x = cos(theta) * sin(phi) * 3
y = cos(theta) * cos(phi) * 2
z = sin(theta)*2

x2 = x*cos(orientation) - y*sin(orientation)
y2 = x*sin(orientation) + y*cos(orientation)

x3 = x*cos(orientation) - z*sin(orientation)+5
z3 = x*sin(orientation) + z*cos(orientation)+5

py.plot([Mesh3d({
                'x': x3.flatten(),
                'y': y2.flatten(),
                'z': z3.flatten(),
                'alphahull': 0}),
    Mesh3d({
        'x': x.flatten(),
        'y': y.flatten(),
        'z': z.flatten(),
        'alphahull': 0})
])