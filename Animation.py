import plotly.offline as py
import numpy as np
import plotly.graph_objs as go
from numpy import cos, sin, pi
# from IPython.display import display, HTML

# init_notebook_mode(connected=True)
phi = np.linspace(0, 2*pi)
theta = np.linspace(-pi/2, pi/2)
phi, theta=np.meshgrid(phi, theta)

orientation=45*pi/180;

x = cos(theta) * sin(phi) * 3
y = cos(theta) * cos(phi) * 2
z = sin(theta)*2

x2 = x*cos(orientation) - y*sin(orientation)
y2 = x*sin(orientation) + y*cos(orientation)

x3 = x*cos(orientation) - z*sin(orientation)
z3 = x*sin(orientation) + z*cos(orientation)

data = go.Data([go.Mesh3d(
                x = x3.flatten(),
                y = y2.flatten(),
                z = z3.flatten(),
                alphahull = 0)])

layout = {'title': 'Ping Pong Animation',
               'xaxis': {'range': [-10, 10], 'autorange': True},
               'yaxis': {'range': [-10, 10], 'autorange': True},
               'updatemenus': [{
                   'buttons': [
                       {'args': [None],
                        'label': 'Play',
                        'method': 'animate'}
               ],
               'pad': {'r': 10, 't': 87},
               'showactive': False,
               'type': 'buttons'
                }]}
frames= [
    {'data': [go.Mesh3d(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        alphahull=0)]
    },
{'data': [go.Mesh3d(
        x=x3.flatten(),
        y=y2.flatten(),
        z=z3.flatten(),
        alphahull=0)]
    },
{'data': [go.Mesh3d(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        alphahull=0)]
    },
{'data': [go.Mesh3d(
        x=[x3.flatten(),x.flatten()],
        y=[y2.flatten(),y.flatten()],
        z=[z3.flatten(),z.flatten()],
        alphahull=[0,0])]
    }
    ]

fig = go.Figure(data=data, layout=layout, frames=frames)
py.plot(fig)

# figure = {'data': [Mesh3d({
#                 'x': x3.flatten(),
#                 'y': y2.flatten(),
#                 'z': z3.flatten(),
#                 'alphahull': 0})],
#           'layout': {'xaxis': {'range': [0, 5], 'autorange': False},
#                      'yaxis': {'range': [0, 5], 'autorange': False},
#                      'title': 'Start Title',
#                      'updatemenus': [{'type': 'buttons',
#                                       'buttons': [{'label': 'Play',
#                                                    'method': 'animate',
#                                                    'args': [None]}]}]
#                     },
#           'frames': [{'data': [{'x': [1, 2], 'y': [1, 2]}]},
#                      {'data': [{'x': [1, 4], 'y': [1, 4]}]},
#                      {'data': [{'x': [3, 4], 'y': [3, 4]}],
#                       'layout': {'title': 'End Title'}}]}
#
# py.plot(figure)